from AbstractDataset import *


class Ioacas(AbstractDataset):
    """docstring for Ioacas."""
    def __init__(self):
        super(Ioacas, self).__init__()
        self._dataset = DATASET_IOACAS
        self._queries = QUERIES_IOACAS
        self._diretorioBase = DIRETORIO_IOACAS

    def _tratarLinhaQuery(self, linhaQuery):
        return (linhaQuery.split('\t'))[0]

    def _obterRespostaCorreta(self, linhaArquivo):
        linhaSplitada = linhaArquivo.rpartition('\t')
        resposta = self._concat(
            self._diretorioBase,
            PASTA_DATASET,
            linhaSplitada[len(linhaSplitada) - 1],
            ".mid"
        )

        return resposta
