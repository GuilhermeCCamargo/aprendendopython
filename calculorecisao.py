import datetime

#Recebendo input do salário bruto

salario = float ( input('Informe o salário bruto: R$ '))

#Recebendo data de admissão

data_adm = input ("Informe a data de Admissão, no formato: dia/mes/ano. Exemplo: 01/07/2020: ")

dia_adm, mes_adm, ano_adm = data_adm.split('/')

data_admissao = datetime.date( int (ano_adm), int (mes_adm), int (dia_adm))

#Recebendo data de demissão

data_dem = input ("Informe a data deDemissão Admissão, no formato: dia/mes/ano. Exemplo: 01/07/2020: ")

dia_dem, mes_dem, ano_dem = data_dem.split('/')

data_demissao = datetime.date( int (ano_dem), int (mes_dem), int (dia_dem))

dias_trabalhados = abs( data_demissao - data_admissao)

resultado_dias = (dias_trabalhados.days)


#Identificando anos, meses e dias trabalhados
anos, resultado_dias = resultado_dias // 365, resultado_dias %365

meses, resultado_dias = resultado_dias // 30, resultado_dias %30

contribuicao_inss =  (salario * 0.08)

total_anos = anos * 12

contribuicao_anos = (total_anos * contribuicao_inss)

contribuicao_meses = (meses * contribuicao_inss)

contribuicao_dias_inss = (contribuicao_inss / 30)

contribuicao_dias = (contribuicao_dias_inss * resultado_dias)

total_fgts = round ((contribuicao_anos + contribuicao_meses + contribuicao_dias), 2)

print ("Seu saldo contribuído ao FGTS é: R$" ,total_fgts)


#print(total_fgts)


#print("Desde {} passaram {} anos, {} meses, {} dias".format(data_demissao, anos, meses, resultado_dias))

