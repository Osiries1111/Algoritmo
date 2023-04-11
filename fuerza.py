fuerza=3
gol=60
dis=0
exponente=0
imprime=''
while dis<gol:
    distancia=(-1*fuerza)**exponente
    dis+=distancia
    if imprime=='':
        imprime+=str(distancia)
    else:
        imprime+=' + '+str(distancia)
    print(imprime,'=',dis)
    exponente+=1
print("Necesite"+exponente+"golpes para alcanzar los"+gol+"metros")