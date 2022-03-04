from numpy import dtype
from Logger import mylogger
import os
import pandas as pd
import shutil
class train_validator:
    def __init__(self,path,config_path,archive_path,correct_path):
        self.path = path 
        self.archive_path = archive_path
        self.correct_path = correct_path
        self.config_path = config_path
        log = mylogger()
    def valid(self):
        for i in os.listdir(self.path):
            if 'csv' in i:
                count = 0
                full_path = self.path+'\\'+i
                raw_data = pd.read_csv(self.path+'\\'+i)
                con =  open(self.config_path).read()
                configs = eval(con)
                emp_list = []
                config_dtypes = configs['ColName']
                for i in config_dtypes:
                    emp_list.append(i)

                for i in range(raw_data.shape[1]):
                    if 'int' or 'float' in raw_data[i].dtype:
                            temp = 'Integer'
                            if emp_list[i] == temp:
                                count += 1
                                if count<24:
                                    continue
                                else:
                                    shutil.move(full_path,self.correct_path)
                                    

                            else:
                                shutil.move(full_path,self.archive_path)
                                break 
                            
          
if __name__ == '__main__':
     trail = train_validator("C:\\Users\\ramka\\Desktop\\Creditcard\\data","C:\\Users\\ramka\\Desktop\\Creditcard\\schema_training.json","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\Archive","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files") 
     trail.valid()  