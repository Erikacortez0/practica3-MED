def obtenerMes(num):
            mes = (
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "octubre", "Noviembre","Diciembre"
            )
            if 1 <= num <= 12:
                nombreMes = mes[num -1]
                return nombreMes
            else:
                return "El mes no existe"
            
numeroMes = int(input("Ingresa un mes: "))
nombreMes = obtenerMes(numeroMes)
print("El mes que corresponde es:", nombreMes)