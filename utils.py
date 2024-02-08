import json

def extract_route(requisicao):
    return requisicao.split()[1][1:]

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()
    
def load_data(arquivo):
    with open(arquivo, 'r') as arquivo_json:
        texto = arquivo_json.read()
        dicionario = json.loads(texto)
        novo_json = json.dumps(dicionario)
        return novo_json

def load_template(arquivo):
    with open('templates/'+ arquivo, 'r') as template_str:
        return template_str.read()
