
import numpy as np
import pandas as pd


def math(a,b):
    print(a + b)

#データセットを作り、それをホールドアウト法、交差確認法、一つ抜き法、ブートストラップ法により、教師データと学習データに分割する
class sample_split():
    """
    col : type=dict,辞書のkeyが行の名前、valueが行の各値 
    """

    def __init__(self,**col):
        self.data = pd.DataFrame(col) 

    def hold_out(self,per):
        num = len(self.data)
        train = self.data.iloc[0:np.int(((per-1)/per)*num)]
        return len(self.data),train

one = [1,2,3,4]
two = [2,4,6,8]
three = [3,6,9,12]
dict = {'one':one,'two':two,'three':three}

a = sample_split(one=one,two=two,three=three)
print(a.hold_out(4)[0])
print(a.hold_out(4)[1])

