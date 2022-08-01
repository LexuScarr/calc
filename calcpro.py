import numexpr

calc = input('Введите выражение: ')
result = numexpr.evaluate(calc)

print(f'Ответ = {result}')
