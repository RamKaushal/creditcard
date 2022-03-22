from Logger import mylogger
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import os
class modelling:
    def __init__(self,model_path):
        self.log = mylogger()
        self.model_path = model_path
    def kmeans_classifier(self):
        df = pd.read_csv(self.model_path)
        df1 = pd.read_csv(self.model_path)
        elist = []
        for i in range(1,10):
            kmeans = KMeans(n_clusters=i)
            kmeans.fit(df)
            elist.append(kmeans.inertia_)
        plt.plot(elist)
        plt.show()
        user_input = int(input("enter number of clusters"))
        kmeans1 = KMeans(n_clusters=user_input)
        kmeans1.fit(df1)
        df1['labels'] = kmeans.labels_
        return df1




        #df['labels'] = kmeans.labels_

if __name__ == '__main__':
    file_path = "C:\\Users\\ramka\\Desktop\\Creditcard\\data\\dataformodel\\"
    file_name = os.listdir("C:\\Users\\ramka\\Desktop\\Creditcard\\data\\dataformodel")[0]
    mod = modelling(file_path+file_name)
    df1 = mod.kmeans_classifier()
    print(df1['labels']['3'])
    print(df1.head(5))