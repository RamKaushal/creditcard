from numpy import dtype, full_like
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
            count = 0
            full_path = self.path+'\\'+i
            raw_data = pd.read_csv(self.path+'\\'+i)
            con =  open(self.config_path).read()
            configs = eval(con)
            dtypes = raw_data.dtypes 
            for i in range(dtypes):
                    if 'int' or 'float' in dtypes[i]:
                        temp = 'Integer'
                        if configs['ColName'][i] == temp:
                            count += 1
                            if count<24:
                                continue
                            else:
                                print("{} is a good file to read".format(full_path))
                                #shutil.move(full_path,self.correct_path)

                        else:
                            print("{} if a corrrupted file at the coulmn {}".format(full_path,configs['ColName'][i]))
                            #shutil.move(full_path,self.archive_path)
                            break 
          
if __name__ == '__main__':
     trail = train_validator("C:\\Users\\ramka\\Desktop\\Creditcard\\data","C:\\Users\\ramka\\Desktop\\Creditcard\\schema_training.json","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\Archive","C:\\Users\\ramka\\Desktop\\Creditcard\\data\\correct_files") 
     trail.valid()               
                

