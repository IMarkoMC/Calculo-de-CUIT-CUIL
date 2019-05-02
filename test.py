print("\x1b[0;33m Calculador de CUIT")

X = 1;

#Array para la entrada de informacion
Test = []

#Array para guardar el resultado de la multiplicacion
Value = []

def CalculateLastDigit(Sex):
    Sum = 0
    if(int(Sex) == 1):
        Value.append((int(2 * 5)))
        Value.append((int(0 * 4)))
    elif int(Sex) == 2:
        Value.append((int(2 * 5)))
        Value.append((int(7 * 4)))
    else:
        print("Error al leer la variable del sexo")

    #Guardar en el array los valores calculados
    index = 0 #Usado para mantener el orden

    #Esquema de multiplicacion
    Multiply= [3,2,7,6,5,4,3,2]

    #Lopear en cada valor del DNI para multiplicarlo por el esquema Multiply
    for x in Test:
        #Insertar en el array de valores el resultado de la multiplicacion
        Value.append((int(Test[index]) * int(Multiply[index])))
        #Aumentar el index en uno
        index +=1

    # Value.append((int(Test[0]) * 3))
    # Value.append((int(Test[1]) * 2))
    # Value.append((int(Test[2]) * 7))
    # Value.append((int(Test[3]) * 6))
    # Value.append((int(Test[4]) * 5))
    # Value.append((int(Test[5]) * 4))
    # Value.append((int(Test[6]) * 3))
    # Value.append((int(Test[7]) * 2))

    #Por cada valor en Value, Sumarlo a la suma general
    for x in Value:
        Sum += x
    
    #Obtener el numero
    Digit = Sum/11

    #Restarle a la suma el digito por once
    PreDig = Sum - (Digit*11)

    #Restartle a 11 el numero calculado para obtener el digito verificador
    Dig =  11 - PreDig

    #Pass to the net function
    Nicify(Dig,Sex)

def Nicify(Dig,Sex):
    #Setear la string del documentos
    i = 0
    while i != 6:
        print #Some blank lines
        i += 1

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    DocString = "{}{}.{}{}{}.{}{}{}".format(Test[0],Test[1],Test[2],Test[3],Test[4],Test[5],Test[6],Test[7])

    print("\x1b[0;33m El CUIT para el documento {} es:".format(DocString))
    if(int(Sex) == 1): #Hombre
        print("20-{}-{}".format(DocString,Dig))
    else: #Mujer
        print("27-{}-{}".format(DocString,Dig))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


#Funcion principal
print("Ingresa tu sexo:")
Sex = raw_input("1- Masculino, 2- Femenino ")
if(Sex != " "): #No dejan la linea en blanco
        if(int(Sex) < 3): #El valor es correcto
            Test = []
            while X != 9: #Pasar por cada digito del documento y pushearlo a un array
                TextInput = raw_input("Ingresa el digito " + str(X) + " de tu DNI ")
                Test.append(TextInput)
                X += 1
            CalculateLastDigit(Sex)
        else:
            print("Sexo invalido!")
else:
    print("Sexo invalido")
