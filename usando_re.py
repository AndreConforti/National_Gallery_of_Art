import re


alfabeto = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')

for letra in alfabeto:
    pagenumber = 1
    pagenumbers = 1
    try:
        url = {'data': re.compile(f"https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/an{letra}.*.htm")}
        print(url)
    except:
        print("Não foi")

