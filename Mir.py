from AbstractDataset import *

class Mir(AbstractDataset):
    """docstring for Mir."""
    def __init__(self):
        super(Mir, self).__init__()
        self._dataset = DATASET_MIR
