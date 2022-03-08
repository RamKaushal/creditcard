from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd
import os
class preprocesss:
    def __init__(self,correct_files_folder):
        self.correct_files_folder = correct_files_folder

    def merge(self):
        merge_list = []
        for i in os.listdir(self.correct_files_folder):
            
            data = pd.read_csv(self.correct_files_folder+"\\"+i)
            merge_list.append(data)
        final_data = pd.concat(merge_list,axis=0,ignore_index=True)
        return final_data
    def null_checker(self,final_data):
        elist = []
        nulls = final_data.isnull().sum()
        for i in nulls.values:
            elist.append(i)
        for i in range(len(elist)):
            if int(elist[i]) >0:
                final_data[i].fillna(final_data[i].mean(),inplace =True,axis = 1)
        return final_data


    
            


if __name__ == '__main__':
    pre = preprocesss('C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files')
    final_data = pre.merge()
    pre.null_checker(final_data)


