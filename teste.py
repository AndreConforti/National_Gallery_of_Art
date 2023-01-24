# Importar bibliotecas
import requests
from bs4 import BeautifulSoup as bs
import csv


# Criar um arquivo CSV para gravar, adicionar linha de cabeçalhos
f = csv.writer(open('a-z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link', 'Nationality', 'Birth', 'Demise'])

alfabeto = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')
pages = []
numbers = []

for letra in alfabeto:
    pagenumber = 1
    pagenumbers = 1

    while pagenumber <= pagenumbers:
        try:
            url = "https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/an" + letra + str(pagenumber) + '.htm'

            # Coletar a página da lista de artistas
            page = requests.get(url)
            # Criar o objeto BeaitufulSoup
            soup = bs(page.text, 'html.parser')

            # Pegar todo o texto da div AlphaNav
            last_links = soup.find(class_='AlphaNav')
            # Pegar o texto de todas as instâncias da tag <a> dentro da div AlphaNav
            page_links = last_links.find_all('a')
            
            pagenumbers = len(page_links) + 1       

        except:
            print("Não existe a página requisitada")
            break
        else:
            # print(f'Coletando as informações da página {letra} - {pagenumber}')
            # last_links.decompose()
            # # Pegar todo o texto da div BodyText
            # lista_artistas = soup.find(class_='BodyText')

            # dados_artistas = lista_artistas.find_all('tr')

            # for linha in dados_artistas:
            #     completo = linha.find_all('td')
            #     nome = completo[0]
            #     nome = nome.find('a')
            #     artist_name = nome.contents[0]
            #     link = 'https://web.archive.org' + nome.get('href')
            #     restante = completo[1].text.split(',')
            #     nationality = restante[0]
            #     try:
            #         periodo = restante[1].split('-')
            #         birth = periodo[0].strip()
            #         demise = periodo[1].strip()
            #     except:
            #         try:
            #             birth = restante[1].strip()
            #             demise = 'Unknown'
            #         except:
            #             nationality = 'Unknown'
            #             birth = 'Unknown'
            #             demise = 'Unknown'
            #     # Adicionar em uma linha o nome de cada artista e o link associado
            #     f.writerow([artist_name, link, nationality, birth, demise])
                        
            pagenumber += 1
            print(pagenumber)
            print(pagenumbers)
  


# url = "https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anA2.htm"
# print(url)

# # Coletar a página da lista de artistas
# page = requests.get(url)
# # Criar o objeto BeaitufulSoup
# soup = bs(page.text, 'html.parser')
# # Pegar todo o texto da div AlphaNav
# last_links = soup.find(class_='AlphaNav')
# last_links.decompose()
# # Pegar todo o texto da div BodyText
# lista_artistas = soup.find(class_='BodyText')

# dados_artistas = lista_artistas.find_all('tr')

# for linha in dados_artistas:
#     completo = linha.find_all('td')
#     nome = completo[0]
#     nome = nome.find('a')
#     nome_artista = nome.contents[0]
#     link = 'https://web.archive.org' + nome.get('href')
#     restante = completo[1].text.split(',')
#     nacionalidade = restante[0]
#     try:
#         periodo = restante[1].split('-')
#         nascimento = periodo[0].strip()
#         falescimento = periodo[1].strip()
#     except:
#         try:
#             nascimento = restante[1].strip()
#             falescimento = 'Unknown'
#         except:
#             nacionalidade = 'Unknown'
#             nascimento = 'Unknown'
#             falescimento = 'Unknown'
#     # Adicionar em uma linha o nome de cada artista e o link associado
#     f.writerow([nome_artista, link, nacionalidade, nascimento, falescimento])











