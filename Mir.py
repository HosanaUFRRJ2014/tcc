from AbstractDataset import *

class Mir(AbstractDataset):
    """docstring for Mir."""
    def __init__(self):
        super(Mir, self).__init__()
        self._dataset = DATASET_MIR
        self._queries = QUERIES_MIR
        self._diretorioBase = DIRETORIO_MIR



    def _obterRespostaCorreta(self, linhaArquivo):
        linhaSplitada = linhaArquivo.rpartition('/')
        resposta = linhaSplitada[len(linhaSplitada) - 1]
        resposta = self._diretorioBase + PASTA_DATASET + resposta.replace("wav","mid")

        return resposta
