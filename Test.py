money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for key in per_cent:
    deposit.append(per_cent[key]*money/100)
    print("deposit =" , deposit)
max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать:"+str(int(max_deposit)))