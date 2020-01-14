#二つの犬の写真をモデルに投入できる型に整形する

import os
import numpy as np
import pandas as pd

class picturesdirectory(self):
    '''
    <USAGE> 
     ex) dir_name = picturesfile() #dir_name:directory which has some pictures to put into models in

    '''

    def __init__(self,dirname);
        self.name = dirname 
        self.pic_inside = os.listdir(dirname)
        


