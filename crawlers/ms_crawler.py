import requests
from lxml import html

class MsCrawler(object):
    def __init__(self):
        self.__session = requests.Session()
    
    def clean_xpath(self, xpath):
        claner = xpath.replace('\n', '')
        claner = claner.replace('\r', '')
        claner = claner.replace('\t', '')
        claner = claner.replace('  ', '')

        return claner

    def get_medicines(self, reg_ms):
        url = "http://sngpc.anvisa.gov.br/consultamedicamento/index.asp"
        payload = "NU_REG={}".format(reg_ms)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
        
        response = self.__session.get(url=url, data=payload, headers=headers)
        if "Número de registro não encontrado na Base de Dados" in response.text:
            return "Número de registro não encontrado na Base de Dados"
        else:
            main_page = html.fromstring(response.text)
            nome_comercial = self.clean_xpath(main_page.xpath('//table[@id="Table1"]//tr[4]/td/text()')[1].replace('\n', ''))
            nome_empresa_detentora = self.clean_xpath(main_page.xpath('//table[@id="Table1"]//tr[5]/td/text()')[1].replace('\n', ''))
            apresentacao_comercial = self.clean_xpath(main_page.xpath('//table[@id="Table1"]//tr[6]/td/text()')[1].replace('\n', ''))
            forma_farmaceutica = self.clean_xpath(main_page.xpath('//table[@id="Table1"]//tr[7]/td/text()')[1].replace('\n', ''))


            return {
                "nome_comercial": nome_comercial,
                "nome_empresa_detentora": nome_empresa_detentora,
                "apresentacao_comercial": apresentacao_comercial,
                "forma_farmaceutica": forma_farmaceutica
            }
