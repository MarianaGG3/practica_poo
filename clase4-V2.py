class Paciente:
    #constructor que inicializa la clase paciente
    def __init__(self):
        #todos los atributos de este constructor presentan un nivel de encapsulamiento de tipo privado
        self.__nombre = "juanita"
        self.__cedula = int
        self.__genero = ""
        self.__servicio = ""

    #nivel de encapsulamiento: privado   
    def verNombre(self):  #get
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    #nivel de encapsulamiento: privado
    def asignarNombre(self,n): #set, que indica la asignacion del nombre del paciente
        self.__nombre = n
    def asignarServicio(self,s): #set, que indica la asignacion del servicio del paciente
        self.__servicio = s
    def asignarGenero(self,g): #set, que indica la asignacion del genero del paciente
        self.__genero = g
    def asignarCedula(self,c): #set, que indica la asignacion del nombre del paciente
        self.__cedula = c

class Sistema:
# en la clase sistema y paciente hay herencia, y posee una relacion de agregacion
    
    #constructor para inicializar la clase sistema llamando a los atributos propios de la instancia
    def __init__(self):
        self.__lista_pacientes = []  #objeto de tipo lista privado para almacenar a los pacientes en el sistema
      
    def eliminarPaciente(self,c):
        if self.verDatosPaciente(c):
            for elim in self.__lista_pacientes:
                if elim==c:
                    self.__lista_pacientes.remove(elim)
      
    def verificarPac(self,ced):
        encontrado =  False
        for p in self.__lista_pacientes:
            if ced == p.verCedula():
                encontrado = True
                #polimorfismo: encontrado cambia de valor segun el objeto encontrado
                break
            elif ced == p.verNombre():
                encontrado = True
                break
              
        return encontrado
        

    def ingresarPaciente(self,pac):
        if self.verificarPac(pac.verCedula()):
            return False
        self.__lista_pacientes.append(pac)
        return True
    
    #funcion para buscar el paciente por cedula, utilizando dos parametros, relacionados con el acceso a los atributos propios (self) y el objeto que me va a permitir buscar a el paciente, y devolverdatos
    def verDatosPaciente(self,c):
        if self.verificarPac(c) == False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p

    def verNumeroPacientes(self):
        #print("Enel sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
    
        return len(self.__lista_pacientes)


    def verDatosxNombre (self, n):
        if self.verificarPac(n) == False:
            print ("el paciente no se encontró")
        else:

            for p in self.__lista_pacientes:
                if n == p.verNombre():
                    print("Nombre: " + p.verNombre())
                    print("Cedula: " + str(p.verCedula()))
                    print("Genero: " + p.verGenero())
                    print("Servicio: " + p.verServicio())

#funcion inicializadora del sistema        
def main():
    sis = Sistema()
    while True:
        opcion = int(input("Ingrese 0 para volver al menu, 1 para ingresar nuevo paciente, 2 ver paciente: , 3 - ver cantidad de pacientes "))
        if opcion == 1:
            print("A continuacion se solicitaran los seguientes datos:")
            # 1 Se solicitaran los datos
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))
            
          #for x in sis.__lista_pacientes:
                #if x==c:   
                    #continue
                #else:
                    #print("este paciente ya ha sido ingresado")
                    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2 se crea un objeto Paciente
            pac = Paciente()
            # como es paciente esta vacio debo ingresarle la informacion
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            r = sis.ingresarPaciente(pac)
            # 3 se almacena en la lista que esta dentro de la clase sistema

            if r == True:
                print("paciente ingresado")
            else:
                print("paciente ya existe en el sistema")

        elif opcion == 2:
            while True:
                menu=int(input("""
                1. buscar paciente por cedula
                2. buscar paciente por nombre:
                """))
                if menu==1:
                    # solicito la cedula que quiero buscar
                    c = int(input("Ingrese la cedula a buscar: "))
                    # le pido al sistema que me devuelva en la variable p al paciente que tenga
                    #  la cedula c en la lista
                    p = sis.verDatosPaciente(c)
                    # si encunetro el paciente imprimo los datos
                    if p == None:
                        print("El paciente no se encontró")
                    else:
                        print("Nombre: " + p.verNombre())
                        print("Cedula: " + str(p.verCedula()))
                        print("Genero: " + p.verGenero())
                        print("Servicio: " + p.verServicio())

                    break
                elif menu==2:
                    # solicito la cedula que quiero buscar
                    c = str(input("Ingrese el nombre a buscar: "))
                    # le pido al sistema que me devuelva en la variable p al paciente que tenga
                    #  la cedula c en la lista
                    b = sis.verDatosxNombre(c)
                    # si encunetro el paciente imprimo los datos
                    print (b)
                    break
              
        elif opcion == 3:
            print(f"la cantidad de pacientes en el sistema es: {sis.verNumeroPacientes()}")
            
            #print(p.lista_pacientes)
                    
        elif opcion != 0:
            continue
        else:
            break

if __name__ == '__main__':
    main()