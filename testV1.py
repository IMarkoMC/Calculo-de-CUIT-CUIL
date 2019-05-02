print("\x1b[0;33m Calculador de CUIT")

X = 1;

#Array para la entrada de informacion
Test = ""

#Array para guardar el resultado de la multiplicacion
Value = []

#Elimianr todos los valores del array antes de recalcular



Sex = 0

def CalculateLastDigit(Sex):

    Sum = 0

    index = 0 #Usado para mantener el orden

    #Esquema de multiplicacion
    Multiply= [3,2,7,6,5,4,3,2]

    #Lopear en cada valor del DNI para multiplicarlo por el esquema Multiply
    while index != len(Test):
        #Insertar en el array de valores el resultado de la multiplicacion
        Value.append((int(Test[index]) * int(Multiply[index])))
        #Aumentar el index en uno
        index +=1


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
    #Obteniendo los primeros dos digitos del array.

    PrimerosDigitos = "{}{}".format(Value[0] /5,Value[1] /4) #Se dividen por 5 y por 4 para obtener el valor inicial

    print("\x1b[0;33m El CUIT para el documento {} es:".format(DocString))
 
    print("{}-{}-{}".format(PrimerosDigitos,DocString,Dig))

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    # Correcto = raw_input("El valor calculado es correcto? Si - No ")
    # print(Correcto)
    # if(Correcto.lower() == "no"): #Ignoro si lo ponen en mayusculas o minusculas
    


#Funcion principal
print("Ingresa tu sexo:")
Sex = raw_input("1- Masculino, 2- Femenino 3- Empresa ")
if(Sex != " "): #No dejan la linea en blanco
        if(int(Sex) < 4): #El valor es correcto
            TextInput = raw_input("Ingresa tu DNI ")
            if(len(TextInput) != 8):
                print('Documento invalido!')
            else:
                if(TextInput.isdigit): #Es numerico y no alguna string random
                    Test = TextInput
                    if(int(Sex) == 1):
                       Value.append((int(2 * 5)))
                       Value.append((int(3 * 4)))
                    elif int(Sex) == 2:
                        Value.append((int(2 * 5)))
                        Value.append((int(7 * 4)))
                    elif int(Sex) == 3:
                        Value.append((int(3 * 5)))
                        Value.append((int(0 * 4)))
                    CalculateLastDigit(Sex)
                else:
                    print('Documento invalido!')
        else:
            print("Sexo invalido!")
else:
    print("Sexo invalido")
