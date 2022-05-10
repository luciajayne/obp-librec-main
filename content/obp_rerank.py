from librec_auto.core.cmd.rerank import Rerank_Helper, User_Helper, Reranker

import numpy as np
import pandas as pd
import pickle
from scipy.spatial import distance
from sklearn.preprocessing import MinMaxScaler
import argparse
from librec_auto.core import read_config_file
import os
import re
from pathlib import Path
from librec_auto.core.util.xml_utils import single_xpath
import warnings
import joblib

warnings.filterwarnings('ignore')
import multiprocessing

from sklearn.preprocessing import LabelEncoder

def get_predictions(learner, new_context):
    # obtains action choice probabilities for the test set
    action_pred_nn_ipw = learner.predict(
        context=new_context
    )

    return action_pred_nn_ipw
def predict_L_from_user_id(user_id, learner,n_actions):
    dim_context = 1
    user_context = np.array(user_id).reshape(-1, dim_context)

    # Run model to predict item list(L) for this user
    action_matrix = get_predictions(learner, user_context).reshape(-1, n_actions)

    # Obtain index and return L record from datafarme
    index = np.argmax(action_matrix, axis=1)

    return index[0]

# class OBD_OFAIR(Reranker):
#
#     def __init__(self, rating, training, rerank_helper):
#         Reranker.__init__(self, rating, training, rerank_helper, self.fun())
#
#     def fun(self):
#         def obd_ofair(rec, rerank_helper, user_helper):
#             num_remain = len(user_helper.item_list)
#             num_curr = len(user_helper.item_so_far)
#
#             if num_curr <= 0:
#                 scores = rerank_helper.lamb * rec
#
#             else:
#                 sim = np.zeros([num_remain, num_curr])
#                 sim_mean = np.zeros(num_remain)
#
#                 for i in range(num_remain):
#                     for j in range(num_curr):
#                         index1 = user_helper.item_list[i]
#                         index2 = user_helper.item_so_far[j]
#                         sim[i][j] = rerank_helper.update_sim_matrix_dic(index1, index2, rerank_helper.binary)
#
#                     sim_mean[i] = np.mean(sim[i])
#                 scores = (1 - rerank_helper.lamb) * rec - rerank_helper.lamb * sim_mean
#
#             return scores, rerank_helper, user_helper
#         return obd_ofair
#




    def entropy(self, labels):
        n_labels = len(labels)
        if n_labels <= 1:
            return 0

        value, counts = np.unique(labels, return_counts=True)
        probs = counts / n_labels
        n_classes = np.count_nonzero(probs)

        if n_classes <= 1:
            return 0

        entropy = -np.sum(np.log2(probs) * probs)
        return entropy,value


    def calculate_weight(self):
        item_feature_df = self.rerank_helper.item_feature_df
        protected = self.rerank_helper.protected

        labels = item_feature_df['feature']
        ent, val = self.entropy(labels)
        weight_dict = {}
        for feature in val:
            if feature in protected:
                weight_dict[feature] = np.sqrt(100 * ent)
            else:
                weight_dict[feature] = np.sqrt(ent)
        self.rerank_helper.weight = weight_dict

        


RESULT_FILE_PATTERN = 'out-(\d+).txt'
INPUT_FILE_PATTERN = 'cv_\d+'


def read_args():
    """
    Parse command line arguments.
    :return:
    """
    parser = argparse.ArgumentParser(description='Generic re-ranking script')
    parser.add_argument('conf', help='Name of configuration file')
    parser.add_argument('original', help='Path to original results directory')
    parser.add_argument('result', help='Path to destination results directory')
    parser.add_argument('--max_len', help='The maximum number of items to return in each list', default=10)
    parser.add_argument('--lambda', help='The weight for re-ranking. Higher lambda means more diversity.')
    parser.add_argument('--binary', help='Whether P(\\bar{s)|d) is binary or real-valued', default=True)
    parser.add_argument('--alpha', help='alpha.')
    parser.add_argument('--protected_feature', help='protected feature')
    parser.add_argument('--method', help='reranking method')

    input_args = parser.parse_args()
    return vars(input_args)


def enumerate_results(result_path):
    pat = re.compile(RESULT_FILE_PATTERN)
    files = [file for file in result_path.iterdir() if pat.match(file.name)]
    files.sort()
    return files


def load_item_features(config, data_path):
    item_feature_file = single_xpath(
        config.get_xml(), '/librec-auto/features/item-feature-file').text
    item_feature_path = data_path / item_feature_file

    if not item_feature_path.exists():
        print("Cannot locate item features. Path: " + item_feature_path)
        return None

    item_feature_df = pd.read_csv(item_feature_path,
                                  names=['itemid', 'feature', 'value'])
    item_feature_df.set_index('itemid', inplace=True)
    return item_feature_df


def output_reranked(reranked_df, dest_results_path, file_path):
    output_file_path = dest_results_path / file_path.name
    print('Reranking for ', output_file_path)
    reranked_df.to_csv(output_file_path, header=False, index=False)


def load_training(split_path, cv_count):
    tr_file_path = split_path / f'cv_{cv_count}' / 'train.txt'

    if not tr_file_path.exists():
        print('Cannot locate training data: ' + str(tr_file_path.absolute()))
        return None

    tr_df = pd.read_csv(tr_file_path, names=['userid', 'itemid', 'score'], sep='\t')

    return tr_df


def execute(rerank_helper, pat, file_path, split_path, dest_results_path):
    tr_df = None

    m = re.match(pat, file_path.name)
    cv_count = m.group(1)
    tr_df = load_training(split_path, cv_count)
    if tr_df is None:
        print("no traning data")
        exit(-1)


    rating_df = pd.read_csv(file_path, names=['userid', 'itemid', 'rating'])

    print("Debug: Reading OBP renranker picke 04-30-22")
    #Pickle lines are replaced with joblib 04-30-22
    with open('OBP_Rerankers.pickle', 'rb') as f:
         learner_dict = pickle.load(f)
    f.close()

    #JobLib Pickle replacement lines
    #learner_dict = joblib.load('OBP_Rerankers.joblib')

    print("Debug: COMPLETED Reading OBP renranker picke 04-30-22")

    learner,item_encoder  = learner_dict["OFAiR"]

    # Convert users to series list
    df_users = pd.DataFrame(rating_df["userid"].unique(), columns=["userID"])

    #Get all unique users
    print("Debug: Predicting users 04-30-22")
    all_users = np.unique(rating_df["userid"]).reshape(-1, 1)
    results = learner.predict(context=all_users)
    print(results.shape)
    #Axis 0 is userid,Axis 1 is itemid,Axis 3 is position
    reranked_df = pd.DataFrame()
    print("Debug: Transforming Data 04-30-22")
    for i,user in enumerate(results):
        list_size = results.shape[2]
        user_id = (np.ones(list_size)*all_users[i]).reshape(-1,1)
        item_ids = item_encoder.inverse_transform(user.T.argmax(axis=1)).reshape(-1,1)
        ratings = np.linspace(0,1,results.shape[2]).reshape(-1,1)
        user_recs = pd.DataFrame(np.concatenate([user_id,item_ids,ratings],axis=1))
        reranked_df = pd.concat([reranked_df,user_recs])

    reranked_df.columns=["userID", "itemID", "rating"]
    reranked_df["userID"] = reranked_df["userID"].astype(int)
    reranked_df["itemID"] = reranked_df["itemID"].astype(int)
    reranked_df = reranked_df.sort_values(by=['userID', 'rating'], ascending=[True, False])

    #reranked_df = pd.concat([df_item, df_rating], axis=1).reset_index().drop("level_1", axis=1)

    # index = df_users.userID.apply(predict_L_from_user_id, args=(learner, len(df_L))).values
    #
    # df_users["L"] = df_L.iloc[index]["L"].values
    # #df_users["L_rating"] = df_L.iloc[index]["L_rating"].values
    #
    # df_users = df_users.set_index("userID")
    # df_item = df_users["L"].str.split(",", expand=True).stack()
    # df_rating = df_users["L_rating"].str.split(",", expand=True).stack()

    #reranked_df = pd.concat([df_item, df_rating], axis=1).reset_index().drop("level_1", axis=1)
    #reranked_df.columns = ["userID", "itemID", "rating"]

    #reranked_df.to_csv(result_file_path, header=None, index=None, sep=',')
    print("Debug: Outputting data 04-30-22")
    output_reranked(reranked_df, dest_results_path, file_path)

    #re_ranker = OBD_OFAIR(rating_df, tr_df, rerank_helper)
    #re_ranker.calculate_weight()

    #reranked_df, rerank_helper = re_ranker.reranker()

    #output_reranked(reranked_df, dest_results_path, file_path)


def main():
    args = read_args()
    config = read_config_file(args['conf'], '.')

    original_results_path = Path(args['original'])
    result_files = enumerate_results(original_results_path)

    dest_results_path = Path(args['result'])

    data_dir = single_xpath(config.get_xml(), '/librec-auto/data/data-dir').text

    data_path = Path(data_dir)
    data_path = data_path.resolve()

    item_feature_df = load_item_features(config, data_path)
    if item_feature_df is None:
        exit(-1)

    # item_helper = set_item_helper(item_feature_df)

    # rerank_helper = set_rerank_helper(args, config, item_helper)
    rerank_helper = Rerank_Helper()
    rerank_helper.set_rerank_helper(args, config, item_feature_df)

    split_path = data_path / 'split'
    pat = re.compile(RESULT_FILE_PATTERN)

    method = args['method']

    p = []

    for file_path in result_files:
        #p1 = multiprocessing.Process(target=execute, args=(
        #    rerank_helper, pat, file_path, split_path, dest_results_path))

        execute(rerank_helper, pat, file_path, split_path, dest_results_path)
        #p.append(p1)
        #p1.start()

    for p1 in p:
        p1.join()


if __name__ == '__main__':
    main()