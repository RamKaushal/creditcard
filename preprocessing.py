from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import pandas as pd
import os
class preprocesss:
    def __init__(self,correct_files_folder):
        self.correct_files_folder = correct_files_folder

    def null_values(self):
        merge_list = []
        for i in os.listdir(self.correct_files_folder):
            
            data = pd.read_csv(self.correct_files_folder+"\\"+i)
            merge_list.append(data)
        final_data = pd.concat(merge_list,axis=0,ignore_index=True)
        print(final_data.head(5))
            


if __name__ == '__main__':
    pre = preprocesss('C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files')
    pre.null_values()


