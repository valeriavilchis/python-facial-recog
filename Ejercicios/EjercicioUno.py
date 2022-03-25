#Creacion de ecuación (c+5)(b2-3ac)a2/4a

value_a = float(input('Ingresa el valor de a: '))
value_b = float(input('Ingresa el valor de b: '))
value_c = float(input('Ingresa el valor de c: '))

one_operation = (value_c + 5)
two_operation = value_b**2
three_operation = 3*(value_a*value_c)
for_operation = value_a**2

result_numerator = (one_operation*(two_operation - three_operation))*for_operation
result_denominator = 4 * value_a
resultt_finally = result_numerator / result_denominator

print(resultt_finally)


