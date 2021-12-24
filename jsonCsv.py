
"""
    O codigo é extremamente simples e sem o uso de qualquer biblioteca, atentar a comentarios para
    saber o que se passa em cada linha, apague ou edite da melhor forma sem alterar as variaveis
"""


#arquivo JSON para ser convertido
data = {
    "cursos": [
        {
            "id": 1,
            "descricao": "Python",
            "valor": 1000
        },
        {
            "id": 2,
            "descricao": "Java",
            "valor": 1500
        },
        {
            "id": 3,
            "descricao": "Swift",
            "valor": 1500
        },
        {
            "id": 4,
            "descricao": "RestFull",
            "valor": 1500
        },
        {
            "id": 5,
            "descricao": "Resct Native",
            "valor": 1500
        }
    ]
 }

# instanciando 
dados = data["cursos"]

#criando uma linha de titulo extraido das chaves do JSON
#(AS Chaves se tornam titulos da tabela)
titulo = []

"""Percorrendo a lista e verificando o fim dela para evitar repeticao
 com isso o codigo so faz um laço e termina a acao salvando o resultado na lista TITULO acima"""
for chave in dados:
    while len(chave) != len(titulo):
        for x in chave:
            titulo.append(x+";")

"""Percorrendo os valores de cada chave listada acima e salvando em suas respectivas colunas
linha por linha """
for chave in dados:
    _id = chave["id"]
    _descricao = chave["descricao"]
    _valor = chave["valor"]
    teste = f"\n{_id};{_descricao};{_valor}"
    titulo.append(teste)

"""Abrindo o arquivos de saida com o resultado da conversao salva na pasta output sendo dois
arquivos JSON e CSV"""
outputJson = open("output/saida.csv", "w")
outputJson.writelines(titulo)
outputJson.close()



"""A partir daqui o codigo pega o arquivo CSV gerado e o converte novamente para JSON"""


arquivoConvertido = open("output/saida.csv", "r")
dados  = arquivoConvertido.readlines()
title = dados[0]
linha = []
linha.append(title.split(";"))
titulo = {linha[0][1], linha[0][0], linha[0][2]}

arquivoConvertido = open("output/saida.csv", "r")
dados  = arquivoConvertido.readlines()
qtd_unid = len(dados)
laco = 1
data = []
while laco != qtd_unid:
    data.append(dados[laco])
    laco +=1
 
lista_tratada = []
convCsvJson = open("output/saidaconv.json", "w")
for b in data:
    lista_tratada.append(b.split(";"))
convCsvJson.writelines("[")

for teste in lista_tratada:
    dicio = {linha[0][0] : teste[0], linha[0][1] : teste[1], linha[0][2] : teste[2]}
    """print('id': teste[0], 'descricao': teste[1], 'valor': teste[1])"""
    convCsvJson.write(str( dicio ))
lista_tratada .append(dicio)
convCsvJson.writelines("]")
print(lista_tratada)



convCsvJson.close()
arquivoConvertido.close()