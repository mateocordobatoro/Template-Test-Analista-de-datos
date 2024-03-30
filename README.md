# README: Análisis de Ofertas Laborales
Este proyecto está diseñado para analizar un conjunto de datos de ofertas laborales, procesando información detallada sobre las ofertas de trabajo y habilidades asociadas. El análisis se realiza a través de un Jupyter Notebook en Google Colaboratory y abarca la carga, procesamiento y presentación de datos relacionados con ofertas laborales.

## Características
Carga de datos desde archivos CSV.
Filtrado y procesamiento de datos basados en criterios específicos como país, nivel de experiencia, fecha de publicación y habilidades requeridas.
Generación de informes sobre ofertas laborales, incluyendo el conteo de ofertas por país y nivel de experiencia, así como el análisis de habilidades solicitadas.
## Uso
Preparación del Entorno
Asegúrese de tener acceso a Google Colaboratory.
Suba los archivos small-jobs.csv y small-skills.csv al entorno de Colab o monte su Google Drive para acceder a los archivos si ya están almacenados allí.
## Ejecución del Análisis
El script realiza los siguientes pasos principales:

### Carga de Ofertas Laborales y Habilidades: Los archivos CSV se leen para obtener los datos de las ofertas laborales y las habilidades requeridas.

### Análisis de Datos: Se ejecutan varias funciones para analizar los datos:

- informe_req1: Filtra las ofertas laborales por país y nivel de experiencia, presentando las últimas N ofertas.
- informe_req2: Clasifica los países con el mayor número de ofertas laborales, analizando adicionalmente las ciudades con más ofertas y las habilidades más solicitadas.
## Resultados
Se generan tablas que presentan las ofertas laborales filtradas por los criterios especificados, así como conteos y análisis de las habilidades requeridas en las ofertas.
## Dependencias
- Python 3
- Bibliotecas: csv, re, datetime, tabulate, collections
- Google Colab (para la ejecución del notebook y manejo de archivos)
## Notas Adicionales
Asegúrese de ajustar las rutas de los archivos y los parámetros de las funciones según sus necesidades y la ubicación de sus archivos CSV.
## Link video 
https://drive.google.com/file/d/1YV8bY3JI2469Le4rmvNsx_c6mXcz2IBH/view?usp=drive_link
