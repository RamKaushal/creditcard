from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
class preprocesss:
    def __init__(self,correct_files_folder):
        self.correct_files_folder = correct_files_folder

    def merge(self):
        merge_list = []
        for i in os.listdir(self.correct_files_folder):
            
            data = pd.read_csv(self.correct_files_folder+"\\"+i)
            data.drop(columns=['ID'],axis=1,inplace=True)
            output = data['default.payment.next.month']
            merge_list.append(data)
        final_data = pd.concat(merge_list,axis=0,ignore_index=True)
        return final_data,output
    def null_checker(self,final_data):
        elist = []
        nulls = final_data.isnull().sum()
        for i in nulls.values:
            elist.append(i)
        for i in range(len(elist)):
            if int(elist[i]) >0:
                final_data[i].fillna(final_data[i].mean(),inplace =True,axis = 1)
        return final_data
    def categoricals(self,final_data):
        label_encode =LabelEncoder()
        final_data_categorical = [i for i in final_data.columns  if final_data.dtypes[i]=='object']
        for i in final_data.columns:
            if i in final_data_categorical:
                final_data[i] = label_encode.fit_transform(final_data[i])
       
        return final_data
    def standard_scalar(self,final_data_to_scale):
        standard = StandardScaler()
        standard.fit_transform(final_data_to_scale)
        return final_data_to_scale
    def pca(self,final_data_after_scaling):
        pca = PCA((final_data_after_scaling.shape[1]) - 1)
        pca.fit(final_data_after_scaling)
        #data_after_pca = pca.transform(final_data_after_scaling)
        initial = 0 
        list_pca = []
        for i in pca.explained_variance_ratio_:
            initial += i 
            list_pca.append(initial)
        print(list_pca)
        plt.plot(list_pca)
        plt.show()
        user_input = int(input("ENTER THE N COMPONENTS OF PCA"))
        new_pca = PCA(n_components=user_input)
        final_data = new_pca.fit_transform(final_data_after_scaling)
        final_data_df = pd.DataFrame(final_data)
        #print(final_data_df.head(5))
        

        
        return final_data_df
    def add_output(self,final_data_after_pca,output_column):
        final_data_after_pca['output'] = output_column
        final_data_after_pca.to_csv("C:\\Users\\ramka\\Desktop\\Creditcard\\data\\dataformodel\\model.csv")
        return final_data_after_pca
    
        


if __name__ == '__main__':
        pre = preprocesss('C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files')
        final_data,output = pre.merge()
        data_with_out_nulls = pre.null_checker(final_data)
        data_categorical = pre.categoricals(data_with_out_nulls)
        data_after_scale1 = pre.standard_scalar(data_categorical)
        after_pca = pre.pca(data_after_scale1)
        final_data_with_column = pre.add_output(after_pca,output)

        

    
            

  


