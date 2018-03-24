from abc import ABCMeta, abstractmethod
from variaveisAmbiente import *
from QueryRespostaCorreta import *

# TODO: Impedir esta classe de ser instanciada
# TODO: Colocar um nome mais claro para esta classe, como AbstractBase, já que lidará com datasets e queries
class AbstractDataset(metaclass=ABCMeta):
    """..."""
    def __init__(self):
        self._listaDataset = []
        self._listaQueries = []
        self._dataset = ""
        self._queries = ""
        self._diretorioBase = ""


    def _abrirArquivo(self,diretorioNomeArquivo):
        arq = open(diretorioNomeArquivo, 'r')
        texto = arq.readlines()
        arq.close()

        return texto


    def _montarListaDataset(self):
        texto = self._abrirArquivo(self._dataset)

        for linha in texto:
            linha = linha.replace("\n","")
            self._listaDataset.append(linha)




    def _tratarLinhaQuery(self, linhaQuery):
        return linhaQuery


    #TODO: Melhorar a escrita desses métodos nas classes filhas
    @abstractmethod
    def _obterRespostaCorreta(self, linhaArquivo):
        pass



    def _montarListaQuery(self):
        texto = self._abrirArquivo(self._queries)

        for linha in texto:
            linha = linha.replace('\n','')
            query = self._diretorioBase + self._tratarLinhaQuery(linha)
            respostaCorreta = self._obterRespostaCorreta(linha)
            queryERespostaCorreta = QueryRespostaCorreta(query,respostaCorreta)
            self._listaQueries.append(queryERespostaCorreta)




    def aplicacao(self):
        #lista = []
        self._montarListaDataset()
        self._montarListaQuery()
    #    print(self._listaDataset)

        i = 0
        while i < 100:
            print(self._listaQueries[i].diretorioNomeArquivoQuery)
            print(self._listaQueries[i].resposta)

            i = i + 1
