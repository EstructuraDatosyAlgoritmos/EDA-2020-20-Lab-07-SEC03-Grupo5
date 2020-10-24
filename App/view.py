"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#crimefile = 'crime-utf8.csv'
accidentsFile = "Accidents/us_accidents_small.csv"
#accidentsFile = "Accidents/US_Accidents_Dec19.csv"
#accidentsFile = "Accidents/us_accidents_dis_2016.csv"
# ___________________________________________________
#  Menu principal
# ___________________________________________________

#Importante datos y corrección laboratorio 5

def printDatos(cont):
    """
    RETO3 - REQ1
    Imprime la información del catálogo.
    """ 
    print('\nAccidentes cargados: ' + str(controller.accidentsSize(cont)))
    print('Fechas de los accidentes: ' + str(controller.yearsSize(cont)))

    print('\nDias en las que ocurrieron accidentes en 2016: ' + str(controller.YearSize_1(cont)[0]))
    print('Altura árbol 2016: ' + str(controller.YearHeight(cont)[0]))

    print('\nDias en las que ocurrieron accidentes en 2017: '+ str(controller.YearSize_1(cont)[1]))
    print('Altura árbol 2017: ' + str(controller.YearHeight(cont)[1]))

    print('\nDias en las que ocurrieron accidentes en 2018: '+ str(controller.YearSize_1(cont)[2]))
    print('Altura árbol 2018: ' + str(controller.YearHeight(cont)[2]))

    print('\nDias en las que ocurrieron accidentes en 2019: '+ str(controller.YearSize_1(cont)[3]))
    print('Altura árbol 2019: ' + str(controller.YearHeight(cont)[3]))

    print('\nDias en las que ocurrieron accidentes en 2020: '+ str(controller.YearSize_1(cont)[4]))
    print('Altura árbol 2020: ' + str(controller.YearHeight(cont)[4]))

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1: conocer accidentes en una fecha")
    print("4- Requerimento 2: Conocer los accidentes anteriores a una fecha")
    print("4- Requerimento 3: Conocer los accidentes en un rango de fechas ")
    print("4- Requerimento 4: Conocer el estado con mas accidentes")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        controller.loadData(cont,accidentsFile)
        printDatos(cont)

    elif int(inputs[0]) == 3:
        print("\nRequerimiento No 1 del reto 3: conocer accidentes en una fecha")
        search_date = input("Ingrese la fecha a buscar:")
        accidents_by_date = controller.getAccidentsByDate(cont,search_date)
        printAccidentsByDate(accidents_by_date,search_date)

    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 2 del reto 3: Conocer los accidentes anteriores a una fecha")
        search_date = input("\nIngrese la fecha desde donde se quieren buscar los accidentes anteriores (En formatoYYYY-MM-DD):")
        accidents_before = controller.getAccidentsBeforeDate(cont,search_date)
        printAccidentsBeforeDare(accidents_before,search_date,cont)
    
    elif int(inputs[0]) == 5:
        print("\nRequerimiento No 3 del reto 3: Conocer los accidentes en un rango de fechas")
        initial_date = input("\nIngrese el límite inferior del rango de fechas (En formato YYYY-MM-DD):")
        final_date = input("\nIngrese el límite superior del rango de fechas (En formato YYYY-MM-DD):")
        accidents_in_range = controller.getAccidentsInRange(cont,initial_date,final_date)
        printAccidentsInRange(cont,initial_date,final_date,accidents_in_range)

    elif int(inputs[0]) == 6:
        print("\nRequerimiento No 4 del reto 3: Conocer el estado con mas accidentes")
        initial_date = input("\nIngrese el límite inferior del rango de fechas (En formato YYYY-MM-DD): ")
        final_date = input("\nIngrese el límite superior del rango de fechas (En formato YYYY-MM-DD): ")
        tuple_result = controller.getState(cont,initial_date,final_date)
        printState(tuple_result)
    else:
        sys.exit(0)
sys.exit(0)

# ___________________________________________________
#  Función que ayuda la impresión de los requerimentos
# ___________________________________________________
def printAccidentsByDate(accidents_by_date,search_date):
    """
    Reto3 - Req1 
    Imprime los accidentes dada una fecha
    """
    if accidents_by_date:
        print("En el día: " + search_date , "Sucedieron:" + str((m.size(accidents_by_date["Accidents_lst"]))) + " accidentes.")
        Map_Severity = accidents_by_date["Severities_mp"]["table"]["elements"]
        for severity in Map_Severity:
            severity_1 = me.getValue(severity)

            if severity_1 is not None:
                iterator = it.newIterator(severity_1["ListBySeverity"])

                print("\nAccidentes y su gravedad: " + str(severity_1["Severity"]))
                while it.hasNext(iterator):
                    accident = it.next(iterator)
                    date_time = datetime.datetime.strptime(accident['Start_Time'], '%Y-%m-%d %H:%M:%S')
                    print("Id: " +  str(accident["Id"]) +  "Datos Fecha:" + str(date_time.ctime()))

def printAccidentsBeforeDare(accidents_before,search,catalog):
    """
    RETO3 - REQ2
    Imprime los accidentes anteriores a una fecha.
    """
    if accidents_before is not None:
        num_acc_before_date = 0
        more_accidents = 0
    
        iterator = it.newIterator(accidents_before)
        while it.hasNext(iterator):
            key_acc = it.next(iterator)
            year_bst = str(key_acc.year)
            day = om.get(catalog[year_bst],key_acc)
            
            num_accidents_in_day =  lt.size(day["value"]["Accidents_lst"])
            num_acc_before_date = num_acc_before_date + num_accidents_in_day

            if num_accidents_in_day > more_accidents:
                more_accidents = num_accidents_in_day
                more_accidents_day = day
    
        print("\nAntes de la fecha ocurrieron: " +  str(num_acc_before_date) + "accidentes.")
        print("El día con mayor cantidad de accidentes fue:" + str(more_accidents_day["key"]) + " Con:" + str(lt.size(more_accidents_day["value"]["Accidents_lst"])) +  "accidentes.")
    else:
        print("La fecha ingresada no es válida.")

def printAccidentsInRange(catalog,initial_date,final_date,accidents_in_range):
    """
    Reto3 - Req3
    Imprime los accidentes en un rango de fechas.
    """    
    if accidents_in_range[0] == 0:
        num_acc_in_range = 0 

        iterator = it.newIterator(accidents_in_range[1])
        while it.hasNext(iterator):
            key_acc = it.next(iterator)
            year_bst = str(key_acc.year)
            day = om.get(catalog[year_bst],key_acc)
    
            num_accidents_in_day =  lt.size(day["value"]["Accidents_lst"])
            num_acc_in_range = num_acc_in_range + num_accidents_in_day
            
        print("\nEntre " +  str(initial_date) + ","+" y "+ str(final_date)+ "sucedieron: " + str(num_acc_in_range)+ "accidentes.")       
    
    
    elif accidents_in_range[0] == 1:
        num_acc_in_range1 = 0 
        num_acc_in_range2 = 0 

        iterator = it.newIterator(accidents_in_range[1])
        while it.hasNext(iterator):

            key_acc = it.next(iterator)
            year_bst = str(key_acc.year)
            day = om.get(catalog[year_bst],key_acc)
    
            num_accidents_in_day =  lt.size(day["value"]["Accidents_lst"])
            num_acc_in_range1 = num_acc_in_range1 + num_accidents_in_day

        iterator2 = it.newIterator(accidents_in_range[2])
        while it.hasNext(iterator2):

            key_acc = it.next(iterator2)
            year_bst = str(key_acc.year)
            day = om.get(catalog[year_bst],key_acc)
    
            num_accidents_in_day =  lt.size(day["value"]["Accidents_lst"])
            num_acc_in_range2 = num_acc_in_range2 + num_accidents_in_day

        print("\nEntre " +  str(initial_date) + ","+" y "+ str(final_date)+" ocurrieron: "+ str(num_acc_in_range1 + num_acc_in_range2)+  "accidentes.")       

    else:
        print("La fecha ingresada no es válida")

def printState(tuple_result):
    """
    Reto3 - Req4
    Imprime el estado con más accidentes en un rango dado.
    """
    if tuple_result is not None:
        print("\nEl estado con más accidentes es: " + str(tuple_result[0]) + ". Con: " + str(tuple_result[1]) + " accidentes.")
        print("La fecha con más accidentes reportados fue: " + str((tuple_result[2])["key"]) + ". Con: " + str(lt.size((tuple_result[2])["value"]["Accidents_lst"])) + " accidentes.")
    else:
        print("La fecha ingresada no es válida")

        
"""
fin
""""