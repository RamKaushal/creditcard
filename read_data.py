import pandas as pd
import os
from Logger import mylogger
class file_read:
    def __init__(self,file_path):
        self.file_path = file_path
        log = mylogger()
    def read_csv(self):
        raw_data = pd.read_csv('')