import time
print("\x1b[0;33m Calculador de CUIT")


global xy #Convertido en global para poder reasignarlo sin problemas

#Esta variable va a guardar los primeros dos digitos, ya sean 20-23-27-30
xy = 0
#String del documento
Test = ""
#Int del sexo
Sex = 0

def CalculateLastDigit():

    Sum = 0

    index = 0 #Usado para mantener el orden

    
    #Agregarle a la suma los dos valores iniciales (20 o 23 o 27 o 30)
    Sum += (int(xy[0]) * 5)
    Sum += (int(xy[1]) * 4)

    #Esquema de multiplicacion
    Multiply= [3,2,7,6,5,4,3,2]

    #Lopear en cada valor del DNI para multiplicarlo por el esquema Multiply
    while index != len(Test):
        #Por cada digito del DNI agregarlo a la suma ya multiplicado
        Sum += (int(Test[index]) * int(Multiply[index]))
        #Aumentar el index en uno
        index +=1
    
    #Obtener el numero
    Div = Sum/11

    #Restarle a la suma el digito por once
    PreDig = Sum - (Div * 11)

    #Restartle a 11 el numero calculado para obtener el digito verificador
    Digit =  11 - PreDig

    #Pass to the net function (Log)
    Nicify(Digit)



def Nicify(Dig):
    #Setear la string del documentos
    i = 0
    while i != 6:
        print #Some blank lines
        i += 1

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    #print()
    #print(Test[2],Test[3],Test[4],Test[5],Test[6],Test[7],Test[8],Test[9])

    DocString = "{}{}.{}{}{}.{}{}{}".format(Test[0],Test[1],Test[2],Test[3],Test[4],Test[5],Test[6],Test[7]) #Pasado a string para agregarle los puntos y que quede mejor

    #print(DocString)
    global xy #Lee el valor de xy global para evitar el error de referenciado antes de asignacion

    print("\x1b[0;33m El CUIT para el documento {} es:".format(DocString))
 
    print("{}-{}-{}".format(xy,DocString,Dig))

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    print #Mas lineas en blanco
    Correcto = raw_input("El valor calculado es correcto? Si - No ")

    if(Correcto.lower() == "no"): #Ignoro si lo ponen en mayusculas o minusculas
        #Recalcular el CUIT con el otro valor posible
        if(int(xy) == 23):
            print('Recalculando cuit....')
            xy = "20"
            CalculateLastDigit()

        elif(int(xy) == 27):
            print('Recalculando cuit....')
            xy = "23"
            CalculateLastDigit()

        elif(int(xy) == 30):

            print('No se puede calcular el cuit con otro valor!')
        
        else:

            print("No se puede calcular el cuit con otro valor!")
    else:
        print("Finalizando...")
        time.sleep(5)
    


#Funcion principal
print("Ingresa tu sexo:")
Sex = raw_input("1- Masculino, 2- Femenino o 3- Empresa ")
if(Sex != " "): #No dejan la linea en blanco
        if(int(Sex) < 4): #El valor es correcto
            TextInput = raw_input("Ingresa tu DNI (Sin puntos ni espacios) ")
            if(len(TextInput) != 8): #No ingresan algun valor random
                print('Documento invalido!')
            else:
                if(TextInput.isdigit): #Es numerico y no alguna string random
                    if(int(Sex) == 1):
                        xy = "23"
                        Test = TextInput
                    elif int(Sex) == 2:
                        xy = "27"
                        Test = TextInput
                    elif int(Sex) == 3:
                        xy = "30"
                        Test = TextInput
                    CalculateLastDigit()
                else:
                    print('Documento invalido!')
        else:
            print("Sexo invalido!")
else:
    print("Sexo invalido")