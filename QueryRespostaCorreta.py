# TODO: implementar get e set, de forma a não permitir setar os parametros pós instanciação
class QueryRespostaCorreta(object):
    """docstring for QueryResultado."""
    def __init__(self, diretorioNomeArquivoQuery, resposta):
        #super(, self).__init__()
        self.diretorioNomeArquivoQuery = diretorioNomeArquivoQuery
        self.resposta = resposta
