from abc import ABCMeta, abstractmethod
from variaveisAbsolutas import *

# TODO: Impedir esta classe de ser instanciada
# TODO: Colocar um nome mais claro para esta classe, como AbstractBase, já que lidará com datasets e queries
class AbstractDataset(metaclass=ABCMeta):
    """..."""
    def __init__(self):
        self._listaDataset = []
        self._listaQueries = []
        self._dataset = ""

    def _abrirArquivo(self,diretorioNomeArquivo):
        arq = open(diretorioNomeArquivo, 'r')
        texto = arq.readlines()
        arq.close()

        return texto


    def _montarListaDataset(self):
        texto = self._abrirArquivo(self._dataset)

        for linha in texto:
            self._listaDataset.append(linha.replace("\n",""))


    #@abstractmethod         #descomentar quando estiver implemetado pra não dar erro
    #def _montarListaQuery(self):
    #    pass


    def aplicacao(self):
        #lista = []
        self._montarListaDataset()
        print(self._listaDataset)
