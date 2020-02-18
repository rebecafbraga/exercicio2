dias_semana = {1: 'domingo', 2: 'segunda', 3: 'terça', 4: 'quarta', 5: 'quinta', 6: 'sexta', 7: 'sabado'}
numero = int(input('digite o numero:' ))
if numero >=1 and numero <=7:
    print(dias_semana[numero])
else:
    print('digite novamente')
