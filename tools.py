
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
        key_list = list(self.col.keys())
        value_list = list(self.col.values())

        shuffled = {}
        for i in range(num):
            a = value_list[i]
            random.shuffle(a)
            shuffled[key_list[i]] = a
        return pd.DataFrame(shuffled)

    def hold_out(self,per):
        num = len(self.data)
        train = self.data.iloc[0:np.int(num*per/100)]
        return len(self.data),train

    def cross_validation(self,m):
        """
        手元の各クラスのデータをそれぞれm個のグループに分割し、m-1個のグループのデータを使って学習し、残りの一つのグループのデータでテストを行う。
        m : データセットを分割する数。
        test_box : テストデータを格納するリスト
        train_box : 学習データを格納するリスト

        *self.data: pd.DataFrame
        """

        length = len(self.data)
        if length % m != 0:
            length = np.int8(length-(length % m))

        test_box = list()
        train_box = list()

        start = 0
        step  = np.int8(length/m)
        end   = step
         
        for i in range(m):
            test_box.append(self.data.iloc[start:end])
            train_box.append(self.data.drop(range(start,end)))

            start += step
            end   += step

        return train_box,test_box

if __name__ =='__main__':
    one = [i for i in range(1,11,1)]
    two = [i for i in range(11,21,1)]
    three = [i for i in range(21,31,1)]
    dict = {'one':one,'two':two,'three':three}

    a = n_sample(one=one,two=two,three=three)
    var1,var2 = a.cross_validation(3)


