
print("O propósito deste arquivo é automatizar a geração de um HTML contendo todos os arquivos de texto em uma página.")
print("Qual é o diretório a ser trabalhado?")
diretorio = input()
print("Qual é o prefixo dos arquivos?")
prefixo = input()
print("Qual é o formato dos arquivos?")
formato = input()
print("Qual é a quantidade de arquivos?")
quantidade = int(input())
print("Qual é o arquivo de estilos do css [com diretório e extensão]?")
estilo = input()
print("Qual deve ser o nome do arquivo de output?")
nome_output = input()
print("Qual deve ser o título do HTML?")
titulo = input()
print("Qual deve ser o prefixo das divs?")
titulo_div = input()

"""
diretorio = "Lista1206"
prefixo = "Questao"
formato = "txt"
quantidade = 3
estilo = "Lista1206/estilo.css"
nome_output = "teste"
titulo = "João Victor Santos"
titulo_div = "Questão"
"""

print("Iniciando o processamento dos arquivos...")
i = 1
div = [""]
while i <= quantidade:
    file = open(diretorio + "/" + prefixo + str(i) + "." + formato)
    div.append("<div>\n<h1>" + titulo_div + " " + str(i) + "</h1>\n")
        
    for line in file:
        div[i] += "\n<p>" + line.split("\n")[0] + "</p>"

    div[i] += "\n</div>\n<hr>\n"
    file.close()
    i += 1

print("Arquivos processados. Criando o HTML...")
html = open(nome_output + ".html", "w")
css = open(estilo)
texto = "<html>\n<head><style>" + css.read() + "</style></head>\n<body>\n<h1>" + titulo + "</h1>\n"
css.close()

for parte in div:
    if parte != "":
        texto += parte

texto += "\n</body>\n</html>"
html.write(texto)
html.close()

print("Finalizado.")
