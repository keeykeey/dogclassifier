
import numpy as np
import pandas as pd
import random

#データセットを作り、それをホールドアウト法、交差確認法、一つ抜き法、ブートストラップ法により、教師データと学習データに分割する
class n_sample():
    """
    col : type=dict,辞書のkeyが行の名前、valueが行の各値 
    """

    def __init__(self,**col):
        self.data = pd.DataFrame(col) 
        self.col =col

    def n_shuffle(self,seed=0):
        random.seed(seed)
        num = len(self.col)
        key_list = list(self.col.key())
        value_list = list(self.col.values())
        for i in range(num):
            


        #    random.shuffle(self.col[i])
        return self.data 

    def hold_out(self,per):
        num = len(self.data)
        train = self.data.iloc[0:np.int(num*per/100)]
        return len(self.data),train

if __name__ =='__main__':
    one = [i for i in range(1,101,10)]
    two = [i for i in range(1,201,20)]
    three = [i for i in range(1,301,30)]
    dict = {'one':one,'two':two,'three':three}

    a = n_sample(one=one,two=two,three=three)
    print(a.col)
    #print(a.n_shuffle())

   # print(a.hold_out(40)[0])
   # print(a.hold_out(40)[1])

