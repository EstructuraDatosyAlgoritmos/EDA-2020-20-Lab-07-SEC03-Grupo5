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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newCatalog_1():
    """ Inicializa el catálogo y
    retorna el catálogo inicializado
    """
    catalog = {'accidents': None,
                "2016": None,
                "2017": None,
                "2018": None,
                "2019": None,
                "2020": None
                }

    catalog["accidents"] = lt.newList("ARRAY_LIST",compareAccidentsId)
    catalog["2016"] = om.newMap(omaptype="BST",comparefunction=CompareDates_Final)                                    
    catalog["2017"] = om.newMap(omaptype="BST",comparefunction=CompareDates_Final)                                  
    catalog["2018"] = om.newMap(omaptype="BST",comparefunction=CompareDates_Final)        
    catalog["2019"] = om.newMap(omaptype="BST",comparefunction=CompareDates_Final)
    catalog["2020"] = om.newMap(omaptype="BST",comparefunction=CompareDates_Final)
                                      
    return catalog
def newCatalog():
    """ Inicializa el catálogo y
    retorna el catálogo inicializado
    """
    catalog = {'accidents': None,
                "2016": None,
                "2017": None,
                "2018": None,
                "2019": None,
                "2020": None
                }

    catalog["accidents"] = lt.newList("ARRAY_LIST",compareAccidentsId)
    catalog["2016"] = om.newMap(omaptype="RBT",comparefunction=CompareDates_Final)                                    
    catalog["2017"] = om.newMap(omaptype="RTB",comparefunction=CompareDates_Final)                                  
    catalog["2018"] = om.newMap(omaptype="RBT",comparefunction=CompareDates_Final)        
    catalog["2019"] = om.newMap(omaptype="RBT",comparefunction=CompareDates_Final)
    catalog["2020"] = om.newMap(omaptype="RBT",comparefunction=CompareDates_Final)
                                      
    return catalog
# Funciones para agregar informacion al catalogo

def addAccident(catalog,accident):
    """
    Adiciona un accidente a la lista de accidentes
    """  
    occurred_start_date = accident["Start_Time"]
    accident_date = datetime.datetime.strptime(occurred_start_date, "%Y-%m-%d %H:%M:%S")
    ocurred_year = str(accident_date.year) 
    lt.addLast(catalog["accidents"],accident)
    uptadeAccidentInDate(catalog[ocurred_year],accident) 
    return catalog 

def newDateEntry():
    """
    Se crea un nodo dada una fecha con sus respectivas llaves
    """
    entry = {"Severities_mp": None, "Accidents_lst": None}
    entry["Severities_mp"] = m.newMap(numelements=15,maptype="PROBING",comparefunction=CompareSeverity_prueba)
    entry["Accidents_lst"] = lt.newList("SINGLE_LINKED", CompareDates_Final)
    return entry

def newSeverityEntry(accident):
    """
    Se crea el grado de gravedad (severity) 
    """
    severity_entry = {"Severity": None, "ListBySeverity": None}
    severity_entry["Severity"] = accident["Severity"]
    severity_entry["ListBySeverity"] = lt.newList("SINGLE_LINKED", CompareSeverity_prueba)
    return severity_entry

def uptadeAccidentInDate(year_map,accident):
    """
    Se busca si existe la fecha del accidente, de no hacerlo la crea
    """
    ocurred_date = accident["Start_Time"]
    accident_date = datetime.datetime.strptime(ocurred_date, "%Y-%m-%d %H:%M:%S")
    entry = om.get(year_map,accident_date.date())

    if entry is None:
        date_entry = newDateEntry()
        
        om.put(year_map,accident_date.date(),date_entry)  
    else:
        date_entry = me.getValue(entry)
    
    addSeverityToDateEntry(date_entry,accident)
    return year_map

def addSeverityToDateEntry(date_entry,accident):
    """
    Actualiza el grado de severidad.
    """
    lt.addLast(date_entry["Accidents_lst"],accident)
    severity = accident["Severity"]
    entry = m.get(date_entry["Severities_mp"], severity)

    if entry != None:

        severity_entry = me.getValue(entry)
        lt.addLast(severity_entry["ListBySeverity"],accident)

    else:
        severity_entry = newSeverityEntry(accident)
        lt.addLast(severity_entry["ListBySeverity"],accident)
        m.put(date_entry["Severities_mp"] , severity, severity_entry)
        
    
    return date_entry

# ==============================
# Funciones de consulta
# ==============================

def getAccidentsByDate(year_bst,search_date):
    """
    Reto3 - Req1
    Retorna el número de accidentes ocurridos en una fecha
    """        

    Accidents_Date = om.get(year_bst,search_date)

    if Accidents_Date["key"] is not None:
        return me.getValue(Accidents_Date)
    
    return None

def getAccidentsBeforeDate(year_RBT,search_date):
    """
    Reto3 - Req2
    Retorna el número de accidentes ocurridos anteriores a una fecha
    """       
    Accidents_Date = om.get(year_RBT,search_date)
    
    if Accidents_Date != None:

        key_date = Accidents_Date["key"]
        keylow = om.minKey(year_RBT)

        return om.keys(year_RBT,keylow,key_date)
    return None

def getAccidentsInRange(catalog,initial_date,final_date):
    """
    Reto3 - Req3
    Retorna el número de accidentes ocurridos en un rango de fechas
    """ 
    initial_year = str(initial_date.year)
    final_year = str(final_date.year)  
    
    if initial_date != None and final_date != None:
        
        if initial_year == final_year:
            
            keylow = om.get(catalog[initial_year],initial_date)["key"]
            keyhigh = om.get(catalog[initial_year],final_date)["key"]
       
            return 0 , om.values(catalog[initial_year],keylow,keyhigh)
        else:

            keymax = om.maxKey(catalog[initial_year])
            dates_initial_year = om.values(catalog[initial_year],initial_date,keymax)

            keymin = om.minKey(catalog[final_year])
            dates_final_year = om.values(catalog[final_year],final_date,keymin)
            return 1 , dates_initial_year , dates_final_year

    return None

def auxiliarPrintFunction(catalog,initial_date,final_date,acc_in_range,criteria):
    """
    Reto3 - Req4
    """
    dictionary = {}
    cont = 1
    
    if acc_in_range[0] == 0 and acc_in_range[1] != None:                     #Primer caso en el que el rango de fechas se encuentra dentro del mismo año 
        condition = 2
    elif acc_in_range[0] == 1 and acc_in_range[1] != None:                  #Segundo caso en el que el rango de fechas abarca dos años
        condition = 3
       
    while cont < condition:
        more_accidents = 0
        num_acc_in_range = 0

        iterator = it.newIterator(acc_in_range[1])
        while it.hasNext(iterator):

            Key_Entry = it.next(iterator)           
            day = om.get(catalog[str(Key_Entry.year)],Key_Entry)
            day_accidents = day['value']['Accidents_lst']

            iterator_acc = it.newIterator(day_accidents)
            while it.hasNext(iterator_acc):
                
                acc = it.next(iterator_acc)
                criteria_dictkey = acc[criteria]
                if criteria_dictkey not in dictionary:
                    dictionary[criteria_dictkey] = 1
                else:
                    dictionary[criteria_dictkey] = dictionary[criteria_dictkey] + 1

            num_accidents_in_day =  lt.size(day_accidents) 
            num_acc_in_range = num_acc_in_range + num_accidents_in_day          #Se calcula el total de accidentes en el rango de fechas.
                
            if num_accidents_in_day > more_accidents:                           #Se calcula el día en el que ocurrieron más accidentes en el rango de fechas.
                more_accidents = num_accidents_in_day
                more_accidents_day = day

def getState(catalog,initial_date,final_date):
    """
    Reto3 - Req4
    Retorna el estado con más accidentes
    """ 
    criteria = "State"
    acc_in_range = getInRange(catalog,initial_date,final_date)
    if acc_in_range != None:
        accidentes_in_range_by_criteria = auxiliarPrintFunction(catalog,initial_date,final_date,acc_in_range,criteria)
        return accidentes_in_range_by_criteria
    return None

def yearsSize(catalog):
    """
    Reto3 - Req1 
    Número de fechas en las que ocurrieron accidentes de todos los años.
    """    
    Año1=om.size(catalog["2016"])
    Año2=om.size(catalog["2017"])
    Año3=om.size(catalog["2018"])
    Año4=om.size(catalog["2019"])
    Año5=om.size(catalog["2020"])
    return Año1 + Año2 + Año3 + Año4, Año5

def YearSize_1(catalog):
    """
    Reto3 - Req1 
    Número de fechas en las que ocurrieron accidentes de
    cada año.
    """    
    Año1=om.size(catalog["2016"])
    Año2=om.size(catalog["2017"])
    Año3=om.size(catalog["2018"])
    Año4=om.size(catalog["2019"])
    Año5=om.size(catalog["2020"])
    return Año1 , Año2 , Año3 , Año4, Año5

def accidentsSize(catalog):
    """
    Reto3 - Req1 
    Número de accidentes.
    """  
    return lt.size(catalog["accidents"])

def YearHeight_1(catalog):
    """
    Reto3 - Req1 
    Altura del árbol de cada año.
    """       
    Año1=om.size(catalog["2016"])
    Año2=om.size(catalog["2017"])
    Año3=om.size(catalog["2018"])
    Año4=om.size(catalog["2019"])
    Año5=om.size(catalog["2020"])

    return Año1, Año2, Año3, Año4, Año5

def statesSize(catalog):
    """
    Reto3 - Req4
    Número de estados cargados.
    """
    return m.size(catalog["States"])

# ==============================
# Funciones de Comparacion
# ==============================

def CompareSeverity_prueba(severity_accident1,severity_accident2):
    """
    Compara la gravedad de accidentes. 
    """
    severity_accident2 = me.getKey(severity_accident2)
    if (severity_accident1 == severity_accident2):
        return 0
    elif (severity_accident1 > severity_accident2):
        return 1
    else:
        return -1

def CompareDates_Final(date1,date2):
    """
    Compara dos fechas de accidentes en años específicos.
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareAccidentsId(id1,id2):
    """
    Compara dos Ids de accidentes. 
    """
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1

