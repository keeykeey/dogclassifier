#main program

import numpy as np
import pandas as pd
import PIL import Image
import os
from collections import OrderedDict,defaultdict,Counter


img_path = os.getcwd()+'/dogs-datas/Images'

class FileError():
    pass
    


def chooseDB():
    try:
        img_dir_list = os.listdir(img_path)
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




