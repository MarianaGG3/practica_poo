class Medicamento:
    def __init__(self):
        #constructor que inicializa la clase medicamento
        self.__nombre = "" 
        self.__dosis = 0 
    #getters
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    #setters
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        #constructor que inicializa la clase mascota
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        #getters
    def verNombre(self):
        #polimorfismo: se usan los mismos nombres de funciones dentro de dos clases diferentes
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
         #setters   
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 

   
    
class sistemaV:
    def __init__(self):
        ##constructor que inicializa la clase sistema
        self.__lista_mascotas = []
        #self.__lista_med=[]
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verificarMedicamento(self,nmed):
        for m in self.__lista_mascotas:
            if nmed == m.verLista_Medicamentos():
                return True

    #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def recuperaMasc (self):
        return self.__lista_mascotas
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 


    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 

    #def eliminarMedicamento (self, emed):
        #for medicina in self.__lista_medicamentos:
            #if emed== medicina.verLista_Medicamentos(Mascota):
                #self.__lista_mascotas.remove(emed)
                #return True
        #return False


def validar(msj):
    while True:
        try:
            valor = int(input(msj))
            break
        except ValueError:
            print("Ingrese un dato numérico...")
def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    lista_med=[]
    
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- eliminar un medicamento
                       \n7- salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
               
                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                mas= Mascota()
                

                for i in range(0,nm):
                   
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    medicamento = Medicamento()
                    for med in lista_med:
                        while True:
                            if med.verNombre()==nombre_medicamentos:
                                print("este medicamento ya existe en el sistema")
                                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                                continue
                            else:
                                break
                
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                        
                        
                            
                        #else:
                        #if servicio_hospitalario.verificarMedicamento(nombre_medicamentos) == False:
                        #dosis =int(input("Ingrese la dosis: "))
                        #medicamento = Medicamento()
                    
                            #mas.asignarLista_Medicamentos(lista_med)(medicamento)
                            #servicio_hospitalario.ingresarMedicamento(mas)

                    
                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

                   

            
            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando

            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) #polimorfismo, diferentes funciones para el mismo objeto medicamento
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
                
                    
                
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:

                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu== 6:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            operacion = servicio_hospitalario.verificarExiste(q) 
            
            
            if servicio_hospitalario.verificarExiste(q)==True:
                
                #ver_mas=servicio_hospitalario.verificarExiste()
                med_elim=input("ingrese el nombre del medicamento a eliminar: ")
                masc=servicio_hospitalario.verMedicamento(med_elim)
                
                if masc== True:
                    medi=masc.verLista_Medicamentos(med_elim)
                    
                    m.remove(medi)
                
                      
                
            else:
                print("No se ha encontrado la mascota")
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

