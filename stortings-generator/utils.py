from typing import Dict
from pandas import read_json, to_datetime, DataFrame
import json
import random
#
def parse_trafo_json(sites_fn:str) -> Dict:
    '''
    Input: full path to the sites JSON files.
    Output: content of the key "data" fof the json file. Must be a Dict.
    '''
    with open(sites_fn,'r',encoding='utf8') as json_fn:
        raw_json = json.load(json_fn)
    return raw_json['data']


def import_data_from_div(data_json) -> DataFrame:
    '''
    Input: Data as JSON.
    Output: Data as Dataframe.
    '''
    # import data
    data_df = read_json(json.loads(data_json),orient='index')

    # Pre-process time column
    # data_df['Time'] = to_datetime(data_df['Time'])
    
    return data_df


def export_data_to_div(data_df: DataFrame) -> Dict:
    '''
    Input: Data as DataFrame.
    Output: Data as JSON.
    '''
    # Export 
    #data_df = data_df.reset_index(drop=False).rename({'index': 'Time'}, axis=1)
    #
    #data_df['Time'] = data_df['Time'].astype(str)
    # import data
    data_json= json.dumps(data_df.to_json(orient='index'))
    
    return data_json


def rnd_to_sum_with_min(desired_sum=169,numbers=3,minimum=5, maximum=60):
    '''
    '''
    selection=[]
    for index in range(numbers-1):
        upper_limit = min(maximum,desired_sum - sum(selection) - (numbers - index) * minimum)
        choice = random.randint(minimum, upper_limit)
        selection.append(choice)
    selection.append(desired_sum-sum(selection))
    return selection