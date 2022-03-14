from Logger import mylogger
from preprocessing import preprocesss
class model:
    def __init__(self,preprocess)
    self.pre = preprocesss()
    final_data = self.pre.merge()
    data_with_out_nulls = self.pre.null_checker(final_data)
    data_categorical = self.pre.categoricals(data_with_out_nulls)
    data_after_scale = self.pre.standard_scalar(data_categorical)
    data_after_pca = self.pre.pca(data_after_scale)
    
    