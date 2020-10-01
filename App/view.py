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
accidentsFile = 'Accidents/us_accidents_small.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1: conocer accidentes en una fecha")
#    print("4- Requerimento 2")
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
        printData(cont)

    elif int(inputs[0]) == 3:
        print("\nBuscando crimenes en un rango de fechas: ")
        

    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 1 del reto 3: conocer accidentes en una fecha")
        search_date = input("Ingrese la fecha a buscar:")
        accidents_by_date = controller.getAccidentsByDate(cont,search_date)
        printAccidentsByDate(accidents_by_date,search_date)
    else:
        sys.exit(0)
sys.exit(0)

# ___________________________________________________
#  Función que ayuda la impresión del req 1
# ___________________________________________________
def printAccidentsByDate(accidents_by_date,search_date):
    """
    Imprime los accidentes dada una fecha
    """
    if accidents_by_date:
        print('En el día: ' + search_date , 'Ocurrieron: ' + str((m.size(accidents_by_date['Accidents_lst']))) + " accidentes."))
        Map_Severity = accidents_by_date['Severities_mp']['table']['elements']
        for severity in Map_Severity:
            severity_1 = me.getValue(severity)

            if severity_1 is not None:
                iterator = it.newIterator(severity_1['ListBySeverity'])

                print('\nAccidentes y su gravedad(severity): ' + str(severity_1['Severity']))
                while it.hasNext(iterator):
                    accident = it.next(iterator)
                    date_time = datetime.datetime.strptime(accident['Start_Time'], '%Y-%m-%d %H:%M:%S')
                    print('Id: ' +  str(accident['Id']) +  ' Datos Fecha: '+ str(date_time.ctime()))