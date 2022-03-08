from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import pandas as pd
import os
import matplotlib.pyplot as plt
class preprocesss:
    def __init__(self,correct_files_folder):
        self.correct_files_folder = correct_files_folder

    def merge(self):
        merge_list = []
        for i in os.listdir(self.correct_files_folder):
            
            data = pd.read_csv(self.correct_files_folder+"\\"+i)
            data.drop(columns=['ID'],axis=1,inplace=True)
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
    def standard_scalar(self,final_data_to_scale):
        standard = StandardScaler()
        standard.fit_transform(final_data_to_scale)
        return final_data_to_scale
    def pca(self,final_data_after_scaling):
        pca = PCA((final_data.shape[1]) - 1)
        pca.fit(final_data_after_scaling)
        data_after_pca = pca.transform(final_data_after_scaling)
        initial = 0 
        list_pca = []
        for i in pca.explained_variance_ratio_:
            initial += i 
            list_pca.append(initial)
        print(list_pca)
        plt.plot(list_pca)
        plt.show()





    
            


if __name__ == '__main__':
    pre = preprocesss('C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files')
    final_data = pre.merge()
    data_with_out_nulls = pre.null_checker(final_data)
    data_after_scale = pre.standard_scalar(data_with_out_nulls)
    data_after_pca = pre.pca(data_after_scale)
    


