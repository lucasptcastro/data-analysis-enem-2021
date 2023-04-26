from dados_candidatos import DadosCandidatos
from dados_regionais import DadosRegionais
from dados_socioeconomicos import DadosSocioeconomicos
from log.logger import Logger

planilha_microdados_enem = './dados/MICRODADOS_ENEM_2021_FORMATADO.csv'

classe_dados_candidatos = DadosCandidatos(planilha_microdados_enem)
classe_dados_regionais = DadosRegionais(planilha_microdados_enem)
classe_dados_socioeconomicos = DadosSocioeconomicos(planilha_microdados_enem)
classe_logger = Logger("ANALISE-ENEM-2021").get_logger()

try:
    print(classe_dados_candidatos.retornar_faixas_etarias_candidatos())
except Exception as error:
    classe_logger.warning('Ocorreu um error: %s', error)