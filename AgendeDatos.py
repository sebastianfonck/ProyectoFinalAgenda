
#------------------- VARIABLES 

#-------------------------- FUNSIONES CRUD -------------------------------
def Listar (agenda):
    
    if len(agenda)>0:
        for contacto, datos in agenda.items():
            print(contacto)
            print(datos[0])
            print(datos[1])
    else:
        print('No hay usuarios ')

def ListarBuscar (agenda):
    

    if (len(agenda)>0):
        nombre = input('Letra: ')
        coincidencias = 0
        
        for contacto, datos in agenda.items():

            words = contacto.split(' ',0)
            character = ''

            for word in words:
                character += word[0]
 
            if nombre in character[0]:
                print(contacto)
                print(datos[0])
                print(datos[1])
                coincidencias += 1
        if coincidencias == 0:
            print('No se encontro usuario')
        else:
            print(coincidencias)
    else:
        print('No hay usuarios ')

def AgregarBeneficiario (agenda,nombre_archivo):
    
    validacion=False
    cedula = (input ("Cedula:"))

    for contacto, datos in agenda.items():
        if cedula == datos[0]:
            validacion=True
        else:
            validacion=False
  
    if validacion==True:
        print('Usuario ya registrado')
    else: 
        nombre = input('Nombre: ')
        celular = input ('Celular : ') 
        agenda.setdefault(nombre,(cedula,celular))
        with open ("C:/Users/sebastian/Desktop/Lore/agenda.txt", 'a') as archivo:
            archivo.write(f'{nombre},{cedula},{celular}\n')
        print('Contacto agregado')

def BuscarBeneficiario (agenda):  
    
    if (len(agenda)>0):
        nombre = input('Nombre: ')
        coincidencias = 0
        for contacto, datos in agenda.items():
            if nombre == contacto:
                print(contacto)
                print(datos[0])
                print(datos[1])
                coincidencias += 1
        if coincidencias == 0:
            print('No se encontro usuario')
        else:
            print(coincidencias)
    else:
        print('No hay usuarios ')

def BorrarBeneficiario (agenda):
    cedula = (input ("Cedula:"))
    for contacto, datos in agenda.items() :
        if cedula == datos[0]:
            print(contacto)
        else:
            print()

#----------------------- OTRAS FUNSIONES
def salir ():
    print()
def error():
    print()

def CrearArchivo (agenda,nombre_archivo):
    
    try:
        with open(nombre_archivo, 'r') :
            v= True
    except FileNotFoundError as e:
        v= False
    except IOError as e:
        v= False


    if(v==False):
        file = open("C:/Users/sebastian/Desktop/Lore/agenda.txt", "w")
    else :
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                contacto,cedula,celualar = linea.strip().split(',')
                agenda.setdefault(contacto,(cedula,celualar))

def menu ():
        print('MENU')
        print ("1. Ver listado")
        print ("2. Ver Listado filtrado")
        print ("3. Agregar beneficiario")
        print ("4. Buscar beneficiario")
        print ("5. Borrar beneficiario")
        print ("6. Salir")

#------------------------- PROGRMA MAIN ---------------

def main ():
    continuar = True
    agenda =dict()
    nombre_archivo='C:/Users/sebastian/Desktop/Lore/agenda.txt'
    CrearArchivo(agenda,nombre_archivo)

    while continuar:
        menu()
        opcion = int(input ("Eligir una opci??n:"))
        
        if (opcion == 1):
            print ("listado de Benefeficiarios")
            Listar (agenda)
        if (opcion == 2):
            print ("Digite la letra por la que empiezan los beneficiarios:")
            ListarBuscar (agenda)
        if (opcion == 3):
            print ("Digite la informaci??n del beneficiario a agregar:")
            AgregarBeneficiario (agenda,nombre_archivo)
        if (opcion == 4):
            print ("Digite el nombre y apellido del beneficiario a buscar:")
            BuscarBeneficiario (agenda)
        if (opcion == 5):
            print ("Digite la cedula del beneficiario a borrar:")
            BorrarBeneficiario (agenda)
        if (opcion == 6):
            salir = True


main()