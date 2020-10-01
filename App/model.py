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

def newCatalog():
    """ Inicializa el catálogo y
    retorna el catálogo inicializado.
    """
    catalog = {'accidents': None,
                '2016': None,
                '2017': None,
                '2018': None,
                '2019': None
                }

    catalog['accidents'] = lt.newList('ARRAY_LIST',compareAccidentsID)
    catalog['2016'] = om.newMap(omaptype='BST',comparefunction=CompareDates_Final)                                    
    catalog['2017'] = om.newMap(omaptype='BST',comparefunction=CompareDates_Final)                                  
    catalog['2018'] = om.newMap(omaptype='BST',comparefunction=CompareDates_Final)        
    catalog['2019'] = om.newMap(omaptype='BST',comparefunction=CompareDates_Final)
                                      
    return catalog

# Funciones para agregar informacion al catalogo

def addAccident(catalog,accident):
    """
    Adiciona un accidente a la lista de accidentes.
    """  
    occurred_start_date = accident['Start_Time']
    accident_date = datetime.datetime.strptime(occurred_start_date, '%Y-%m-%d %H:%M:%S')
    ocurred_year = str(accident_date.year) 
    lt.addLast(catalog['accidents'],accident)
    uptadeAccidentInDate(catalog[ocurred_year],accident) 
    return catalog 

def newDateEntry():
    """
    Se crea un nodo dada una fecha con sus respectivas llaves.
    """
    entry = {'Severities_mp': None, 'Accidents_lst': None}
    entry['Severities_mp'] = m.newMap(numelements=15,maptype='PROBING',comparefunction=CompareSeverity_prueba)
    entry['Accidents_lst'] = lt.newList('SINGLE_LINKED', CompareDates_final)
    return entry

def newSeverityEntry(accident):
    """
    Se crea el grado de gravedad (severity) 
    """
    severity_entry = {'Severity': None, 'ListBySeverity': None}
    severity_entry['Severity'] = accident['Severity']
    severity_entry['ListBySeverity'] = lt.newList('SINGLE_LINKED', CompareSeverity_prueba)
    return severity_entry

def uptadeAccidentInDate(year_map,accident):
    """
    Se busca si existe la fecha del accidente, de no hacerlo la crea
    """
    ocurred_date = accident['Start_Time']
    accident_date = datetime.datetime.strptime(ocurred_date, '%Y-%m-%d %H:%M:%S')
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
    lt.addLast(date_entry['Accidents_lst'],accident)
    severity = accident['Severity']
    entry = m.get(date_entry['Severities_mp'], severity)

    if entry is None:
        severity_entry = newSeverityEntry(accident)
        lt.addLast(severity_entry['ListBySeverity'],accident)
        m.put(date_entry['Severities_mp'] , severity, severity_entry)
    else:
        severity_entry = me.getValue(entry)
        lt.addLast(severity_entry['ListBySeverity'],accident)
    
    return date_entry

# ==============================
# Funciones de consulta
# ==============================

def getAccidentsByDate(year_ven,search_date):
    """
    Retorna el número de accidentes ocurridos en una fecha.
    """        

    date_accidents = om.get(year_ven,search_date)

    if date_accidents['key'] is not None:
        return me.getValue(date_accidents)
    
    return None
    
def yearsSize(catalog):
    """
    Número de fechas en las que ocurrieron accidentes de todos los años.
    """    
    Año1=om.size(catalog['2016'])
    Año2=om.size(catalog['2017'])
    Año3=om.size(catalog['2018'])
    Año4=om.size(catalog['2019'])
    
    return Año1 + Año2 + Año3 + Año4

def YearSize_1(catalog):
    """
    Número de fechas en las que ocurrieron accidentes de
    cada año.
    """    
    Año1=om.size(catalog['2016'])
    Año2=om.size(catalog['2017'])
    Año3=om.size(catalog['2018'])
    Año4=om.size(catalog['2019'])

    return Año1 , Año2 , Año3 , Año4

def accidentsSize(catalog):
    """
    Número de accidentes.
    """  
    return lt.size(catalog['accidents'])

def YearHeight_1(catalog):
    """
    Altura del árbol de cada año.
    """       
    Año1 = om.height(catalog['2016'])
    Año2 = om.height(catalog['2017'])
    Año3 = om.height(catalog['2018'])
    Año4 = om.height(catalog['2019'])

    return Año1, Año2, Año3, Año4

# ==============================
# Funciones de Comparacion
# ==============================

def CompareSeverity_prueba(severity_accident1,severuty_accident2):
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

def CompareDates_final(date1,date2):
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