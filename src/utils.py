import sys
import os
import pandas as pd
import numpy as np
import pickle
from src.exception import CustomException
from src.logger import logging
import pickle

def save_object(file_path,obj):
    try:
        # dir_path = os.path.dirname(file_path),
        # os.makedirs(dir_path,exist_ok = True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        logging.info('Object saved successfully')  

    except Exception as e:
        raise CustomException(e,sys)    

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e,sys)      