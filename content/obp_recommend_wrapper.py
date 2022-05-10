#Name: Zijun Liu
#File: Deep Learning Recommendation Algorithm
#CIKM 2021

import argparse
import pandas as pd
import numpy as np
import pickle
from pathlib import Path
from librec_auto.core.util.xml_utils import single_xpath
from librec_auto.core import read_config_file

# from recommenders.reco_utils.recommender.cornac.cornac_utils import predict_ranking


def read_args():
    parser = argparse.ArgumentParser(description='nnRec')
    parser.add_argument('conf', help='Name of configuration file')
    parser.add_argument('train', help='Path to training data file')
    parser.add_argument('test', help='Path to test data file')
    parser.add_argument('result', help='Path to destination results file')
    parser.add_argument('--model', choices=['OBP_STANDARD','OBP_FAIR','OBP_RANDOM'])
   
    input_args = parser.parse_args()
    return vars(input_args)


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

    return index[0]  #df.iloc[index][["L","L_rating"]].values[0]

def random_L_from_user_id(user_id,n_actions):

    return np.random.choice(list(range(n_actions)))

def main():
    args = read_args()
    model = args['model']
    config = read_config_file(args['conf'], '.')
    if (args["model"] is None):
        model = single_xpath(config.get_xml(), '/librec-auto/alg/script/param[@name="model"]').text
    else:
        model = args['model']

    training_path = args['train']
    test_path = args['test']
    result_file_path = Path(args['result'])

    #Select users in training set
    train_df = pd.read_csv(training_path, sep="	", header=None)
    train_df.columns = ["userID", "itemID", "rating"]
    unique_users = sorted(train_df.userID.unique())
    unique_users = np.random.permutation(unique_users)

    #Convert users to series list
    df_users = pd.DataFrame(unique_users, columns=["userID"])
    userSeries = df_users["userID"]

    if model == 'OBP_STANDARD':
        with open('IPW_OBP_demo02.pickle', 'rb') as f:
            learner, df_L = pickle.load(f)
        f.close()
        index = userSeries.apply(predict_L_from_user_id, args=(learner, len(df_L))).values

    elif model == 'OBP_FAIR':
        with open('IPW_OBP_demo01.pickle', 'rb') as f:
            learner, df_L = pickle.load(f)
        f.close()
        index = userSeries.apply(predict_L_from_user_id, args=(learner, len(df_L))).values

    elif model == 'OBP_RANDOM':
        with open('OBP_random.pickle', 'rb') as f:
            learner, df_L = pickle.load(f)
        f.close()
        index = userSeries.apply(random_L_from_user_id, args=(len(df_L),)).values


    df_users["L"] = df_L.iloc[index]["L"].values
    df_users["L_rating"] = df_L.iloc[index]["L_rating"].values

    df_users = df_users.set_index("userID")
    df_item = df_users["L"].str.split(",", expand=True).stack()
    df_rating = df_users["L_rating"].str.split(",", expand=True).stack()

    df_rev = pd.concat([df_item, df_rating], axis=1).reset_index().drop("level_1", axis=1)
    df_rev.columns = ["userID", "itemID", "rating"]
    df_rev = df_rev.sort_values(by=['userID', 'rating'], ascending=[True, False])

    df_rev.to_csv(result_file_path, header=None, index=None, sep=',')

      

if __name__ == '__main__':
    main()