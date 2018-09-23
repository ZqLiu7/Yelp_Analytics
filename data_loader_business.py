import json
import pandas as pd
import ast
from collections import defaultdict


def load_business_data_df(file_path='yelp_academic_dataset_business.json'):
    with open(file_path, 'r') as json_file:
        all_attributes = get_all_attributes(json_file)
    with open(file_path, 'r') as json_file:
        data_dict = process_business_data(json_file, all_attributes)
    return pd.DataFrame(data_dict)


def get_all_attributes(json_file):
    all_attributes = set()
    for line in json_file:
        for key_level_1, value_level_1 in json.loads(line).items():
            if type(value_level_1) != dict:
                all_attributes.add(key_level_1)
            else:
                for key_level_2, value_level_2 in value_level_1.items():
                    if len(value_level_2) > 0 and value_level_2[0] == '{':
                        sub_data = ast.literal_eval(value_level_2)
                        for key_level_3, value_level_3 in sub_data.items():
                            composite_key = key_level_1 + '_' + key_level_2 + '_' + key_level_3
                            all_attributes.add(composite_key)
                    else:
                        composite_key = key_level_1 + '_' + key_level_2
                        all_attributes.add(composite_key)
    return all_attributes


def process_business_data(json_file, all_attributes):
    '''
    :param all_attributes: all the attributes existed in the dataset
    :return: a defaultlist which contains all the data
    '''
    business_data = defaultdict(list)
    for line in json_file:
        for key_level_1, values_level_1 in json.loads(line).items():
            attribute_set = set()
            if type(values_level_1) != dict:
                business_data[key_level_1].append(values_level_1)
                attribute_set.add(key_level_1)
            else:
                for key_level_2, values_level_2 in values_level_1.items():
                    if len(values_level_2) > 0 and values_level_2[0] == '{':
                        sub_data = ast.literal_eval(values_level_2)
                        for key_level_3, values_level_3 in sub_data.items():
                            composite_key = key_level_1 + '_' + key_level_2 + '_' + key_level_3
                            business_data[composite_key].append(values_level_3)
                            attribute_set.add(composite_key)
                    else:
                        composite_key = key_level_1 + '_' + key_level_2
                        business_data[composite_key].append(values_level_2)
                        attribute_set.add(composite_key)
            null_variable = list(all_attributes - attribute_set)
            for key in null_variable:
                business_data[key].append('')
    return business_data