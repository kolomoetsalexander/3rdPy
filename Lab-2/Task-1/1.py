import pandas as pd
#чтение
data = pd.read_csv('transactions.csv')

# Задача 1: Найдите 3 самых крупных платежа из реально проведённых (статус OK).
bigest = data[
    data['STATUS'] == 'OK'
            ].nlargest(3, 'SUM')  #из DF data выбираем строки у которых статус равно ок
                                  #из отфильтрованных строк выбираем 3 строки с наибольшим значением в столбце сум

#сортируем по убыванию
big_sort = bigest.sort_values(by='SUM', ascending=False)

print("Топ 3 самых крупных платежа из реально проведённых:")

#итерируем по каждой строке
for index, row in big_sort.iterrows():
    print(f"{row['CONTRACTOR']} - {row['SUM']}") #для каждой строки извлекаем значения столбцов контрактор и сум

# Задача 2: Определите полную сумму реально проведённых платежей в адрес Umbrella, Inc.
#фильтруем по столбцу контрактор, оставляем только строки, где'Umbrella, Inc', а по стат, оставляем только ок
total_umbrella = data[
    (data['CONTRACTOR'] == 'Umbrella, Inc') & (data['STATUS'] == 'OK')
                        ]['SUM'].sum()
print(f"Полная сумма реально проведенных платежей в адрес Umbrella, Inc: {total_umbrella}")