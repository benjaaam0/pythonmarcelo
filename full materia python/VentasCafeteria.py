pan_ciabatta = 2000
pie_de_limon = 3500
cafe = 2200
alfajor = 1000

print("--------INFORME DE VENTAS--------")

print("-----Ventas del dia lunes-----")

pan_ciabatta = 2000*50
print(f"la ventas del pan ciabatta fue: {pan_ciabatta}")
pie_de_limon = 3500*40
print(f"la ventas del pie de limon fue: {pie_de_limon}")
cafe = 2200*60
print(f"las ventas de cafe fue: {cafe}")
te = 1600*45 
print(f"las ventas de te fue: {te}")
alfajor = 1000*55
print(f"las ventas de alfajor fue:{alfajor}")

total_lunes = pan_ciabatta + pie_de_limon + cafe + te + alfajor
print(f"tu total de ventas del dia lunes fue: {total_lunes}")

print("-----Ventas del dia martes-----")

pan_ciabatta = 2000*30
print(f"la ventas del pan ciabatta fue: {pan_ciabatta}")
pie_de_limon = 3500*25
print(f"la ventas del pie de limon fue: {pie_de_limon}")
cafe = 2200*35
print(f"las ventas de cafe fue: {cafe}")
te = 1600*28
print(f"las ventas de te fue: {te}")
alfajor = 1000*32
print(f"las ventas de alfajor fue:{alfajor}")

total_martes = pan_ciabatta + pie_de_limon + cafe + te + alfajor
print(f"tu total de ventas del dia martes fue: {total_martes}")

print("-----Ventas del dia miercoles-----")

pan_ciabatta = 2000*20
print(f"la ventas del pan ciabatta fue: {pan_ciabatta}")
pie_de_limon = 3500*15
print(f"la ventas del pie de limon fue: {pie_de_limon}")
cafe = 2200*25
print(f"las ventas de cafe fue: {cafe}")
te = 1600*18
print(f"las ventas de te fue: {te}")
alfajor = 1000*22
print(f"las ventas de alfajor fue:{alfajor}")

total_miercoles = pan_ciabatta + pie_de_limon + cafe + te + alfajor
print(f"tu total de ventas del dia miercoles fue: {total_miercoles}")

print("-----Ventas del dia jueves-----")

pan_ciabatta = 2000*10
print(f"la ventas del pan ciabatta fue: {pan_ciabatta}")
pie_de_limon = 3500*8
print(f"la ventas del pie de limon fue: {pie_de_limon}")
cafe = 2200*12
print(f"las ventas de cafe fue: {cafe}")
te = 1600*9
print(f"las ventas de te fue: {te}")
alfajor = 1000*11
print(f"las ventas de alfajor fue:{alfajor}")

total_jueves = pan_ciabatta + pie_de_limon + cafe + te + alfajor
print(f"tu total de ventas del dia martes fue: {total_jueves}")

print("-----INFORME TOTAl DE VENTAS-----")

total_semana = total_lunes + total_martes + total_miercoles + total_jueves 
print(f"total de venta de la semana fue: {total_semana}")