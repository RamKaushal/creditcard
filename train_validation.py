from numpy import dtype
from Logger import mylogger
import os
import pandas as pd
import shutil
class train_validator:
    def __init__(self,path,config_path,archive_path,correct_path):
        """
        input paramas:
        Path:path of csv file
        config_path:path of config_path
        archive_path:path of folder where the bad files will go
        correct_path:path of folder where the good files end up
        outputs 
        none:
        """
        self.path = path 
        self.archive_path = archive_path
        self.correct_path = correct_path
        self.config_path = config_path
        log = mylogger()
    def valid(self):
        """
        input: none
        desc:iterates through the folder where csv files are present, checks the dtype of the columns with the schema file of the client to maintain the data quality according to the data sharing agreement and moves the file to good and bad folders based on the quality check
        """
        for i in os.listdir(self.path):
            if 'csv' in i:
                count = 0
                full_path = self.path+'\\'+i
                raw_data = pd.read_csv(self.path+'\\'+i)
                self.log.logmessage('read the file'+full_path)
                con =  open(self.config_path).read()
                configs = eval(con)
                self.log.logmessage('read the config file'+self.config_path)
                emp_list = []
                dtypes_list = []
                config_dtypes = configs['ColName']
                for i in config_dtypes:
                    emp_list.append(i)
                for i in raw_data.dtypes.values:
                    dtypes_list.append(i)
                
                
                for i in range(raw_data.shape[1]):
                    if 'int' or 'float64' in dtypes_list[i]:
                                count += 1
                                if count<25:
                                    continue
                            
                                else:
                                    shutil.move(full_path,self.correct_path)
                                    self.log.logmessage("file {} moved to accepted folder".format(full_path))
                                    print("file moved to accepted folder")

                    else:
                                shutil.move(full_path,self.archive_path)
                                self.log.logmessage("file {} moved to rejected folder as the column {} is different".format(full_path,emp_list[i]))
                                print("file is incorrect at column {}".format(emp_list[i]))
                                break 
               
                           
          
if __name__ == '__main__':
     trail = train_validator("C:\\Users\\ramka\\Desktop\\Creditcard\\data","C:\\Users\\ramka\\Desktop\\Creditcard\\schema_training.json","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\Archive","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files") 
     trail.valid()  