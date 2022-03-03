from numpy import dtype
from Logger import mylogger
import os
import pandas as pd
import shutil
class train_validator:
    def __init__(self,path,archive_path,correct_path):
        self.path = path 
        self.archive_path = archive_path
        self.correct_path = correct_path
        log = mylogger()
    def valid(self):
        for i in os.listdir(self.path):
            count = 0
            full_path = self.path+'\\'+i
            raw_data = pd.read_csv(self.path+'\\'+i)
            con =  open(self.path).read()
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
                                shutil.move(full_path,self.correct_path)

                        else:
                            shutil.move(full_path,self.archive_path)
                            break 
          
                 
                

