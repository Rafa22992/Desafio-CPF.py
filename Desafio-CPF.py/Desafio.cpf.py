"""
----------------------------
CPF:168-995-350/09
----------------------------
1 * 10 = 10
6 * 9 = 54
8 * 8 = 64
9 * 7 = 63
9 * 6 = 54
5 * 5 = 25
3 * 4 = 12
5 * 3 = 15
0 * 2 = 0
----------
  total 297
  formula = 11- (297 % 11) = 11
  -----------------------------
  condição
  if 11 > 9
   digito_1 = 0
  else
   digito_1 = formula
"""
cpf_padrão = [1,6,8,9,9,5,3,5,0,0,9] #CPF a ser checado em IF
cpf = '168995350' #CPF a ser interado em FOR
novo_cpf = [1,6,8,9,9,5,3,5,0] # CPF que irá receber os 2 ultimos digitos
s = 10
resut = []
soma = 0
formula = 0

for d in cpf:

 if not len(cpf) < 9:
     d = int(d)
     total = s * d
     resut.append(total)
     s -= 1
     soma += total
     digito_1 = 11 - (soma % 11)

     if digito_1 > 9:
         digito_1 = 0

     else:
         digito_1

novo_cpf.append(digito_1)
print(f' Novo CPF com 1°Digito {novo_cpf}')

#----------- FIM PRIMEIRO DIGITO------------------------

#---------------SEGUNDO DIGITO ------------------------------
s_2 = 11
resul_2 = []
soma_2 = 0
for d_2 in novo_cpf:

    if not len(novo_cpf) < 10:
        d_2 = int (d_2)
        total_2 = d_2 * s_2
        resul_2.append(total_2)
        s_2 -= 1
        soma_2 += total_2
        digito_2 = 11 - (soma_2 % 11)

        if digito_2 > 9:
            digito_2 = 0

        else:
            digito_2
novo_cpf.append(digito_2)
print(50*'*')
print(f'Novo CPF completo {novo_cpf}')

if novo_cpf == cpf_padrão:
    print(50*'*')
    print('CPF Válido')
else:
    print('CPF Inválido')