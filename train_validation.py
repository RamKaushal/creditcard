from Logger import mylogger

class train_validator:
    def __init__(self,path):
        self.path = path 
        log = mylogger()
    def valid(self):
        con =  open(self.path).read()
        configs = eval(con)
        print(configs['ColName']['LIMIT_BAL'])
        return None

if __name__ == '__main__':
    train = train_validator("C:\\Users\\ramka\\Desktop\\Creditcard\\schema_training.json")
    train.valid()