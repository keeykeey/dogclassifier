
import numpy as np
import pandas as pd


def math(a,b):
    print(a + b)

#データセットを作り、それをホールドアウト法、交差確認法、一つ抜き法、ブートストラップ法により、教師データと学習データに分割する
class sample():
    def __init__(self,**col):
        self.data = pd.DataFrame(col) 

    def hold_out(percentager):
        num = len(col) 











one = [1,2,3,4]
two = [2,4,6,8]
three = [3,6,9,12]

a = sample(one=one,two=two,three=three)
print(a.data)






