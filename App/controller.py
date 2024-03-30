
import config as cf
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    pass


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass





# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
################################################################################################## SOLUCION ################################################################
# librerias
import csv
import re
from datetime import datetime
from tabulate import tabulate
from collections import Counter

file1 = 'small-jobs.csv'
file2 = 'small-skills.csv'
file3 = 'small-multilocations.csv'


### lectura

def lectura_data(file_names):
    lineas = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        if omitir_encabezado:
            next(archivo)  # Omitir los encabezados
        for linea in archivo:
            lineas.append(linea.strip())
    return lineas




jobs = lectura_data(file1)
skills = lectura_data(file_names2)
multilocations = lectura_data(file_names3)

#### jobs

jobs_dic = []
jobs_excluidos = []

lista_encabezados = encabezados.split(';')

for job in jobs:
    # Aplica el reemplazo para manejar el ';' dentro de las URLs antes de dividir el trabajo en elementos
    patron = r'"([^"]*http[s]?://[^;]+); ([^"]+)"'
    reemplazo = lambda match: '"' + match.group(1) + ' or ' + match.group(2) + '"'
    job_modificado = re.sub(patron, reemplazo, job)

    # Convertir cada trabajo modificado en una lista para comparar longitudes
    lista_job = job_modificado.split(';')

    if len(lista_job) == len(lista_encabezados):
        # Si coinciden en longitud, se crea el diccionario de trabajos
        diccionario_trabajo = dict(zip(lista_encabezados, lista_job))

        # Convertir 'published_at' a un objeto datetime
        if 'published_at' in diccionario_trabajo:
            diccionario_trabajo['published_at'] = datetime.strptime(diccionario_trabajo['published_at'], "%Y-%m-%dT%H:%M:%S.%fZ")

        # Añadir al diccionario de trabajos a la lista jobs_dic
        jobs_dic.append(diccionario_trabajo)
    else:
        # Si no coinciden en longitud, ajusta según necesites. Aquí simplemente se agregan a jobs_excluidos.
        job_modificado2 = re.sub(r'"([^"]*);([^"]*)"', r'"\1, \2"', job)
        lista_job = job_modificado2.split(';')
        diccionario_trabajo = dict(zip(lista_encabezados, lista_job))
        if 'published_at' in diccionario_trabajo:
            diccionario_trabajo['published_at'] = datetime.strptime(diccionario_trabajo['published_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
        jobs_excluidos.append(diccionario_trabajo)

jobs_complete = jobs_dic + jobs_excluidos

tabla_hash = {diccionario['id']: diccionario for diccionario in jobs_complete}


### skills


contenido_skills = [skill.split(';') for skill in skills]
encabezados_skills = ['Habilidades','Nivel_experiencia','id']
skills = [dict(zip(encabezados_skills, skill)) for skill in contenido_skills]
tabla_hash_skills = {skill['id']: skill for skill in skills}



paises_unicos = set(oferta['country_code'] for oferta in tabla_hash.values())

for job_id, job_info in tabla_hash.items():
  if job_id in tabla_hash_skills:
    job_info.update(tabla_hash_skills[job_id])

### multilocations

multilocations = [elemento.split(';') for elemento in multilocations]
encabezados3 = ['City','Street','id']
multilocations = [dict(zip(encabezados3, location)) for location in multilocations]

tabla_hash_multilocations = {}
for location in multilocations:
  location_id = location['id']
  if location_id in tabla_hash_multilocations:
    tabla_hash_multilocations[location_id]['num_sedes'] += 1
  else:
    tabla_hash_multilocations[location_id]= {'num_sedes': 1}

for job_id, job_info in tabla_hash.items():
  if job_id in tabla_hash_multilocations:
    job_info.update(tabla_hash_multilocations[job_id])

return tabla_hash



def informe_req1(ofertas, num_ofertas, codigo_pais, nivel_experiencia):
    # Calcular paises_unicos directamente de las ofertas
    paises_unicos = set(oferta['country_code'] for oferta in ofertas.values())

    # Validación
    if codigo_pais not in paises_unicos:
        return "No hay ofertas laborales registradas para ese país."

    niveles_experiencia_validos = {'junior', 'mid', 'senior'}
    if nivel_experiencia not in niveles_experiencia_validos:
        return "Nivel de experiencia no válido."

    # Filtrar ofertas por país y nivel de experiencia y contar las ofertas por nivel de experiencia

    ofertas_pais = [oferta for oferta in ofertas.values()
                         if oferta['country_code'] == codigo_pais]

    ofertas_filtradas = [oferta for oferta in ofertas.values()
                         if oferta['country_code'] == codigo_pais
                         and oferta['experience_level'] == nivel_experiencia]

    conteo_nivel_experiencia = sum(1 for oferta in ofertas_filtradas if oferta['experience_level'] == nivel_experiencia)

    # Ordenar ofertas filtradas por fecha de publicación de manera descendente
    ofertas_filtradas.sort(key=lambda x: x['published_at'], reverse=True)

    # Resultados
    ultimas_n_ofertas = ofertas_filtradas[:num_ofertas]
    ultimas_n_ofertas = ultimas_n_ofertas

    try:
        from tabulate import tabulate
        t1 = tabulate(ultimas_n_ofertas, headers="keys", tablefmt="grid")
    except ImportError:
        t1 = "Error: La librería 'tabulate' no está instalada. Por favor, instálela para visualizar la tabla."

    return print(f"- El total de ofertas de trabajo ofrecidas para {codigo_pais} son {len(ofertas_pais)} \n- En la tabla a continuación se presentan las últimas {num_ofertas} ofertas de trabajo para el nivel de experiencia {nivel_experiencia}. \n- El total de ofertas de trabajo ofrecidas para este nivel de experiencia fue un total de {conteo_nivel_experiencia}.\n {t1}" )

#informe_req1(ofertas= tabla_hash, num_ofertas = 10, codigo_pais = 'GB', nivel_experiencia = 'junior')

def informe_req2(ofertas, num_paises, anio, mes):
    # Validación de año y mes
    if anio not in [2022, 2023] or mes < 1 or mes > 12:
        print("No hay ofertas laborales para la fecha que desea consultar.")
        return

    # Filtrado de ofertas por fecha
    ofertas_filtradas = [
        oferta for oferta in ofertas.values()
        if oferta['published_at'].year == anio and oferta['published_at'].month == mes
    ]

    if not ofertas_filtradas:
        print("No se encontraron ofertas laborales para el periodo especificado.")
        return



    # Conteo de ofertas por país usando comprensión de lista y Counter
    conteo_ofertas_por_pais = Counter(oferta['country_code'] for oferta in ofertas_filtradas)
    ofertas_por_pais = conteo_ofertas_por_pais.most_common(num_paises)

    conteo_ciudades_por_pais = {
        pais: len({oferta['city'] for oferta in ofertas_filtradas if oferta['country_code'] == pais})
        for pais, _ in ofertas_por_pais
    }

    # Conteo de ofertas por ciudad dentro de cada país
    ofertas_por_ciudad = {
        pais: Counter(oferta['city'] for oferta in ofertas_filtradas if oferta['country_code'] == pais)
        for pais, _ in ofertas_por_pais
    }
    ciudades_max_ofertas = [
        (pais, ciudad.most_common(1)[0][0], ciudad.most_common(1)[0][1])
        for pais, ciudad in ofertas_por_ciudad.items()
    ][:10]

    # Procesamiento de información agrupada por país y nivel de experiencia

    agrupacion = {
        pais: {
            oferta['experience_level']: {
                'habilidades': Counter(oferta.get('Habilidades', 'Unknown')),
                'empresas': Counter([oferta['company_name']]),
                'niveles_experiencia': [int(oferta.get('Nivel_experiencia', 0))]
            }
            for oferta in ofertas_filtradas if oferta['country_code'] == pais
        }
        for pais, _ in ofertas_por_pais
    }

    niveles_experticia = ['junior', 'mid', 'senior']

# Estructura para acumular los datos
    datos_por_nivel = {
    nivel: {
        'habilidades': Counter(),
        'empresas': Counter(),
        'niveles_habilidad': [],
    }
    for nivel in niveles_experticia
    }


    for oferta in ofertas_filtradas:  # ofertas_filtradas es la lista de ofertas de trabajo
      nivel = oferta['experience_level']
      if nivel in datos_por_nivel:
        # Acumular conteo de habilidades

        datos_por_nivel[nivel]['habilidades'][oferta['Habilidades']] += 1
        # Acumular conteo de empresas
        datos_por_nivel[nivel]['empresas'][oferta['company_name']] += 1

        # Acumular niveles de habilidad (asumiendo que esto es un número en la oferta)
        datos_por_nivel[nivel]['niveles_habilidad'].append(oferta.get('Nivel_experiencia', 0))

    resultados = {}

    for nivel, datos in datos_por_nivel.items():
      habilidades = datos['habilidades']
      empresas = datos['empresas']
      niveles_habilidad = datos['niveles_habilidad']
      niveles_habilidad = [int(x) if x!= '' else 0 for x in niveles_habilidad]

      habilidad_mas_solicitada = habilidades.most_common(1)[0]
      habilidad_menos_solicitada = sorted([(habilidades, conteo) for habilidades, conteo in habilidades.most_common() if conteo == 1],key=lambda x: x[0])
      habilidad_menos_solicitada = habilidad_menos_solicitada[:10] if len(habilidad_menos_solicitada) > 1 else habilidades.most_common()[-1]
      nivel_minimo_promedio = sum(niveles_habilidad) / len(niveles_habilidad)
      empresa_mas_ofertas = empresas.most_common(1)[0]
      empresa_menos_ofertas = sorted([(empresa, conteo) for empresa, conteo in empresas.most_common() if conteo == 1],key=lambda x: x[0])[0:10]
      empresa_menos_ofertas = empresa_menos_ofertas[:10] if len(empresa_menos_ofertas) > 1 else empresas.most_common()[-1]
      num_empresas = len(empresas)


      resultados[nivel] = {
          'conteo_habilidades': len(habilidades),
          'habilidad_mas_solicitada' : habilidad_mas_solicitada,
          'habilidad_menos_solicitada' : habilidad_menos_solicitada,
          'nivel_minimo_promedio' : nivel_minimo_promedio ,
          'empresa_mas_ofertas' : empresa_mas_ofertas,
          'empresa_menos_ofertas' : empresa_menos_ofertas,
          'num_empresas' : num_empresas
          }





    # Impresión de resultados
    print(f"-El total de las ofertas de empleo registradas en el mes {mes} del año {anio} es {len(ofertas_filtradas)}.")
    print("-En la tabla a continuación se puede observar los países con la mayor cantidad de ofertas laborales para el mes seleccionado:")
    print(tabulate(ofertas_por_pais, headers=['Cod Pais', 'Num ofertas'], tablefmt="grid"))
    print("- Ciudades con la mayor cantidad de ofertas laborales:")
    print(tabulate(ciudades_max_ofertas, headers=['Cod Pais', 'Ciudad', 'Num Ofertas'], tablefmt="grid"))
    print("- Número de ciudades donde se ofertó por pais:")
    print(conteo_ciudades_por_pais) ################################################## PONER FORMATO TABLA

    for nivel, datos in resultados.items():
      print("-------------------------------------------------------------------------------------------------------------------------")
      print(f"Nivel de experticia: {nivel}")
      print("-------------------------------------------------------------------------------------------------------------------------")

      print(f"  Habilidades diferentes solicitadas: {datos['conteo_habilidades']}")
      print(f"  Habilidad más solicitada: {datos['habilidad_mas_solicitada'][0]}, conteo: {datos['habilidad_mas_solicitada'][1]}")
      print(f"  Habilidad menos solicitada:\n {tabulate(datos['habilidad_menos_solicitada'])}")
      print(f"  Nivel mínimo promedio de habilidades: {datos['nivel_minimo_promedio']:.2f}")
      print(f"  Número de empresas diferentes: {datos['num_empresas']}")
      print(f"  Empresa con mayor número de ofertas: {datos['empresa_mas_ofertas'][0]}, ofertas: {datos['empresa_mas_ofertas'][1]}")
      print(f"  Empresas con menor número de ofertas:\n {tabulate(datos['empresa_menos_ofertas'])}")
      print("-------------------------------------------------------------------------------------------------------------------------")


#informe_req2(ofertas=tabla_hash, num_paises=10, anio=2022, mes=10)

