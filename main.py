#main program

import numpy as np
import pandas as pd
import PIL import Image
import os
from collections import OrderedDict,defaultdict,Counter


img_path = os.getcwd()+'/dogs-datas/Images'

class FileError():
    pass
    

def chooseDB(kind,another_kind):
'''
dog1 : a kind of dog you want to classify from 'dog'
dog2 :another kind of dog you want to classify from 'dog'  
'''
    try:
        img_dir_list = os.listdir(img_path)
        for i in range(len(img_dir_list)):
            if (dog1 or dog2) in img_dir_list[i]:
                dog1 = 
    except:
        raise FileErroe 


def sample():
    pass





def create_model():
    pass

def predict():
    pass


if __name__ == "__main__":
    predict()




