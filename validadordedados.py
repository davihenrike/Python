sexo = (input('Informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in  'MF':
    sexo = (input('Dados inválidos, por favor informe seu genero com M para masculino e F para feminino.')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
