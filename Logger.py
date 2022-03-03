
import logging
class mylogger:
    def __init__(self):
        pass
    def logmessage(self,message):
# Create and configure logger
        self.message = message
        logging.basicConfig(filename="creditcard.log",format='%(asctime)s %(message)s',filemode='a')
        logger = logging.getLogger()
        logger.warning(self.message)
        return self.message 

if __name__ == '__main__':
    log = mylogger()
    b = log.logmessage("testing the loggger")
    print(b)
