#36% descuento en compra final

one_price = float(input("Ingrese el precio del primer articulo: "))
two_price = float(input("Ingrese el precio del segundo articulo: "))
three_price = float(input("Ingrese el precio del tercer articulo: "))

buys_total = one_price + two_price + three_price

discount = (36 * buys_total / 100)

finally_price = buys_total - discount

print(f'El precio final con descuento es: ${finally_price}')