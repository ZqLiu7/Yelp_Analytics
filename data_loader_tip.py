import json
import pandas as pd
import ast
from collections import defaultdict


def load_tip_data_df(file_path='yelp_academic_dataset_tip.json'):
    with open(file_path, 'r') as json_file:
        all_attributes = get_all_attributes(json_file)
    with open(file_path, 'r') as json_file:
        data_dict = process_tip_data(json_file, all_attributes)
    return pd.DataFrame(data_dict)


def get_all_attributes(json_file):
    all_attributes = set()
    for line in json_file:
        for key_level_1, value_level_1 in json.loads(line).items():
            all_attributes.add(key_level_1)
    return all_attributes


def process_tip_data(json_file, all_attributes):
    '''
    :param all_attributes: all the attributes existed in the dataset
    :return: a defaultlist which contains all the data
    '''
    tip_data = defaultdict(list)
    for line in json_file:
        attribute_set = set()
        for key_level_1, values_level_1 in json.loads(line).items():
            tip_data[key_level_1].append(values_level_1)
            attribute_set.add(key_level_1)
    return tip_data