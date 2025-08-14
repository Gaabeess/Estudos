total_segundos = int(input("Digite o tempo em segundos: "))                      # conversão de string para inteiro

dias = total_segundos // 86400  # cálculo de dias
horas = (total_segundos % 86400) // 3600  # cálculo de horas
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60  # cálculo de segundos restantes

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")    # exibição do resultado
