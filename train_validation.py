from numpy import dtype
from Logger import mylogger
import os
import pandas as pd
import shutil
class train_validator:
    #def __init__(self,path,config_path,archive_path,correct_path):
    def __init__(self,path):
        self.path = path 
        log = mylogger()
    def valid(self):
        for i in os.listdir(self.path):
            print(i)
            """
            count = 0
            full_path = self.path+'\\'+i
            raw_data = pd.read_csv(self.path+'\\'+i)
            print(raw_data.head(5))
            
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
                                shutil.move(full_path,self.correct_path)

                        else:
                            shutil.move(full_path,self.archive_path)
                            break 
            """
          
if __name__ == '__main__':
     trail = train_validator("C:\\Users\\ramka\\Desktop\\Creditcard\\data") 
     trail.valid()               
                

