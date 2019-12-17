#main program

import numpy as np
import pandas as pd
from PIL import Image
import os
from collections import OrderedDict,defaultdict,Counter


img_path = os.getcwd()+'/dogs-datas/Images'


class FileError():
    pass
    

def chooseDB(dog1,dog2):
    '''
    dog1 : a kind of dog you want to classify from 'dog'
    dog2 :another kind of dog you want to classify from 'dog'  
    '''

    try:
        img_dir_list = os.listdir(img_path)
        for i in range(len(img_dir_list)):
            if dog1  in img_dir_list[i]:
                dog1_path = img_path + img_dir_list[i] 
                checkpoint += 1
            elif dog2 in img_dir_list[i]:
                dog2_path = img_path + img_dir_list[i]    
                checkpoint +=1
        if checkpoint <2 :
            print('We don\'t have {} or {} file in the directory <{}>'.format(dog1,dog2,img_path))
 
    except:
        raise FileErroe 

    return dog1_path,dog2_path



def sample():
    pass





def create_model():
    pass

def predict():
    pass


if __name__ == "__main__":
    predict()




