import datetime

#Verificações a se fazerque mudam o cálculo: se a demissao foi por justa causa, valor do desconto de FGTS de acordo com faixa salárial

#Recebendo input do salário bruto

#Boas vindas

print ("Seja Bem Vindo! \n")

salario = float ( input('\n Informe o salário bruto: R$ '))

opcao = int ( input("\n Foi Justa Causa? \n \n 0-Sim 1-Não \n \n"))

if(opcao > 1):
	
	print("\n Digite um número válido!! \n")
	
	exit()

elif (opcao == 0):
	
	multa_fgts = (salario * 0.40)
else:
	multa_fgts = 0

#Recebendo data de admissão

data_adm = input ("\n Informe a data de Admissão, no formato: dia/mes/ano. \n \n Exemplo: 01/07/2020: \n \n")

dia_adm, mes_adm, ano_adm = data_adm.split('/')

data_admissao = datetime.date( int (ano_adm), int (mes_adm), int (dia_adm))

#Recebendo data de demissão

data_dem = input ("\n Informe a data de Demissão Admissão, no formato: dia/mes/ano. \n \n Exemplo: 01/07/2020: \n \n")

dia_dem, mes_dem, ano_dem = data_dem.split('/')

data_demissao = datetime.date( int (ano_dem), int (mes_dem), int (dia_dem))

dias_trabalhados = abs( data_demissao - data_admissao)

resultado_dias = (dias_trabalhados.days)


#Identificando anos, meses e dias trabalhados
anos, resultado_dias = resultado_dias // 365, resultado_dias %365

meses, resultado_dias = resultado_dias // 30, resultado_dias %30

contribuicao_inss =  (salario * 0.08)

#Calculando o total da contribuição para o FGTS, levando em conta que a pessoa não receba mais que um salário mínimo e meio por mês.

total_anos = anos * 12

contribuicao_anos = (total_anos * contribuicao_inss)

contribuicao_meses = (meses * contribuicao_inss)

contribuicao_dias_inss = (contribuicao_inss / 30)

contribuicao_dias = (contribuicao_dias_inss * resultado_dias)

total_fgts = round ((contribuicao_anos + contribuicao_meses + contribuicao_dias + multa_fgts), 2)

#print ("Seu saldo contribuído ao FGTS é: R$" ,total_fgts)

#Calculando o Décimo Terceiro a Receber

decimo_mensal = ((salario) / 12)

decimo_a_receber_por_mes = ((decimo_mensal * meses))

valor_do_dia = (decimo_mensal / 30)

decimo_a_receber_por_dia = (valor_do_dia * resultado_dias)

decimo_total_a_receber = round ((decimo_a_receber_por_mes + decimo_a_receber_por_dia), 2)

#Se o funcionário trabalho um ano exato o valor a receber vai estar zerado
#print ("Valor total a receber de 13º terceiro: R$", decimo_total_a_receber)

#Cálculo de férias a receber

terco_a_somar = (salario / 3)

valor_dia_trabalhado = ((salario / 30))

valor_a_receber_por_dias = ((resultado_dias * valor_dia_trabalhado))

valor_a_receber_por_mes = ((meses * decimo_mensal))

valor_a_receber_por_ano = (salario)

#incluir verificação se foi justa causa ou não, e verificação se foi um ano completo de trabalho
ferias_total = round ( (valor_a_receber_por_dias + valor_a_receber_por_mes) + terco_a_somar)

#Calculando salário a receber por dias trabalhados

salario_por_dia = (salario / 30)

salario_por_dia_a_receber = round ((salario_por_dia * resultado_dias), 2)

a_receber = round ((decimo_total_a_receber + ferias_total + salario_por_dia_a_receber), 2)

print ("\n Seu saldo contribuído ao FGTS é: R$" ,total_fgts)

print ("\n Valor total a receber de 13º terceiro: R$", decimo_total_a_receber)

print ("\n Você deverá receber pelas férias: R$", ferias_total)

print ("\n A empresa deve te pagar o valor total de: R$",a_receber)

#print(total_fgts)


#print("Desde {} passaram {} anos, {} meses, {} dias".format(data_demissao, anos, meses, resultado_dias))

