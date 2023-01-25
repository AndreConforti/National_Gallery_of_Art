# Importar bibliotecas
import requests
from bs4 import BeautifulSoup as bs
import csv
from time import sleep
import pandas as pd


# Criar um arquivo CSV para gravar, adicionar linha de cabeçalhos

alfabeto = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')
pages = []
numbers = []
artists = []

for letra in alfabeto:
    for number in range(1, 100):
        url = "https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/an" + letra + str(number) + '.htm'
        sleep(5)
        ## Coletar a página da lista de artistas
        page = requests.get(url)
        if page.status_code == 200:          
            print(f'Coletando as informações da página {letra} - {number}')
            ## Criar o objeto BeaitufulSoup
            soup = bs(page.text, 'html.parser')
            ## Pegar todo o texto da div AlphaNav e excluir
            last_links = soup.find(class_='AlphaNav') 
            last_links.decompose()
            ## Pegar todo o texto da div BodyText
            lista_artistas = soup.find(class_='BodyText')

            dados_artistas = lista_artistas.find_all('tr')

            for linha in dados_artistas:
                completo = linha.find_all('td')
                nome = completo[0]
                nome = nome.find('a')
                artist_name = nome.contents[0]
                link = 'https://web.archive.org' + nome.get('href')
                restante = completo[1].text.split(',')
                nationality = restante[0]
                try:
                    periodo = restante[1].split('-')
                    birth = periodo[0].strip()
                    demise = periodo[1].strip()
                except:
                    try:
                        birth = restante[1].strip()
                        demise = 'Unknown'
                    except:
                        nationality = 'Unknown'
                        birth = 'Unknown'
                        demise = 'Unknown'
                ## Adicionar em uma linha o nome de cada artista e o link associado
                artist = {
                    'artist_name' : artist_name,
                    'link' : link,
                    'nationality' : nationality,
                    'birth' : birth,
                    'demise' : demise
                }
                artists.append(artist.copy())
        else:
            print("Página não encontrada")
            break
    break
                        
df = pd.DataFrame(artists)

df.to_csv('artistas_a_z.csv', sep=(';'))


