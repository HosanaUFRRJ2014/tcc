from AbstractDataset import *

class Ioacas(AbstractDataset):
    """docstring for Ioacas."""
    def __init__(self):
        super(Ioacas, self).__init__()
        self._dataset = datasetIocas

        #return listaDataset
