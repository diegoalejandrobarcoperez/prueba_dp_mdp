import logging
import pandas as pd
import sqlite3 
import pyodbc 
import os
import openpyxl
import schedule
import time

logging.basicConfig(filename='LOG.log', format='%(asctime)s %(message)s', datefmt='%Y%m%d %H:%M:%S %p', level=logging.DEBUG)


##ruta = (r'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2') para el config

##----------------------------------------------------------------------------------------------
################### AGREGAR HOJA DE EXCEL A BASE DE DATOS DE MS ACCES #################
##----------------------------------------------------------------------------------------------


## Abrir el archivo de excel con openpy para crear las tuplas que irán en la tabla de access
excel =  openpyxl.load_workbook(r'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\CATALOGO_CLASE.xlsx')
tabla = 'CATALOGO_CLASE'    ##Nombre que tendra la tabla en la base de datos
hoja_activa = excel.active

##----------------------------------------------------------------------------------------------
##-------------------- Realiza la concexión con MS ACCESS con el modulo pyodc
##----------------------------------------------------------------------------------------------
##   print(driver) -Para ver los Drivers

try:
    conn_string = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ= C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\bases_datos.accdb;')
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()

    logging.info('[SUCCESS]: Se ha realizado la conexión con la base de datos de MS ACCESS')
except Exception as e:
    logging.error('[ERROR]: No se ha realizado la conexión con la base de datos de MS ACCESS')



## Se crea la funcion que permite guardar los datos del archivo de excel como tuplas
datos_excel = []
for fila in hoja_activa.iter_rows(values_only = True):
    datos_excel.append(fila)
excel.close()

## se crea la tabla y se agrega el nombre de las columnas
try:
    sql_crear_tabla = f"CREATE TABLE {tabla} ("  
    nombres_columnas = datos_excel[0]
    for nombre_columna in nombres_columnas:
        sql_crear_tabla+= f"{nombre_columna} TEXT,"
    sql_crear_tabla = sql_crear_tabla.rstrip(',')
    sql_crear_tabla+= ')'
    cursor.execute(sql_crear_tabla)
    logging.info('[SUCCESS]: Se ha creado la tabla con el nombre CATALOGO_CLASE')
except Exception as e:
    logging.error('[ERROR]: No se ha creado la tabla con el nombre CATALOGO_CLASE')

## Insertar los datos apartir de las segunda fila en la tabla creada
try:
    sql_insertar = f"INSERT INTO {tabla} VALUES ("
    for fila_datos in datos_excel[1:]:
        valores_fila = ",".join([f"'{valor}'" for valor in fila_datos])
        cursor.execute(f"{sql_insertar}{valores_fila})")
    conn.commit()
    logging.info('[SUCCESS]: Se han insertado los datos a la tabla CATALOGO_CLASE')
except Exception as e:
    logging.error('[ERROR]: No se han insertado los datos a la tabla CATALOGO_CLASE')

## Conocer el nombre de las tablas almacenadas en el archivo de Access
for nombre in cursor.tables(tableType='TABLE'):
    print (nombre.table_name)

##----------------------------------------------------------------------------------------------
### ----------------------------FUNCION QUE PERMITE LEER LOS ARCHIVOS .SQL 
##----------------------------------------------------------------------------------------------
def leer_archivos_sql(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido



##----------------------------------------------------------------------------------------------
### ----------------------------PROGRAMAR EJECUCIÓN A LAS 8:00 AM
##----------------------------------------------------------------------------------------------
def tarea_programada_8():
    try:
        ##------------------------------------------------------------------------------------------------------------------
        ## -----------------------------------CREAR TABLA EN MS ACCESS PARA EL PUNTO 1-------------------------------------
        ##--------------------------Cantidad de tarjetas activas de tarjeta débito por clase de tarjeta.
        ##-----------------------------------------------------------------------------------------------------------------
        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\Crear_tablas\\punto_1.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
                    
            cursor.execute(contenido_sql)
            logging.debug('[SUCCESS]: Se ha creado la tabla punto_1')
        except Exception as e:
            logging.error('[ERROR]: No se ha creado la tabla punto_1')

        ##------------------------------------------------------------------------------------------------------------------
        ## ------------------------INSERTAR LOS DATOS DEL PRIMER CURECE EN LA TABLA PUNTO_1 CREADA ANTERIORMENTE-------------
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\SQL1.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
            cursor.execute(contenido_sql)
            conn.commit()
            logging.info('[SUCCESS]: Se ha insertado el resultado del query SQL1 en la tabla punto_1')
        except Exception as e:
            logging.error('[ERROR]: No se ha insertado el resultado del query SQL1 en la tabla punto_1')


        ##------------------------------------------------------------------------------------------------------------------
        ## -----------------------------------CREAR TABLA EN MS ACCESS PARA EL PUNTO 2-------------------------------------
        ##--------------------------Cantidad de tarjetas inactivas de MasterDebit por descripción de clase de tarjeta.
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\Crear_tablas\\punto_2.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
                
            cursor.execute(contenido_sql)
            logging.info('[SUCCESS]: Se ha creado la tabla punto_2')
        except Exception as e:
            logging.error('[ERROR]: No se ha creado la tabla punto_2')

        ##------------------------------------------------------------------------------------------------------------------
        ## ------------------------INSERTAR LOS DATOS DEL PRIMER CURECE EN LA TABLA PUNTO_2 CREADA ANTERIORMENTE-------------
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\SQL2.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
            cursor.execute(contenido_sql)
            conn.commit()
            logging.info('[SUCCESS]: Se ha insertado el resultado del query SQL2 en la tabla punto_2')
        except Exception as e:
            logging.error('[ERROR]: No se ha insertado el resultado del query SQL2 en la tabla punto_2')

        ##------------------------------------------------------------------------------------------------------------------
        ## -----------------------------------CREAR TABLA EN MS ACCESS PARA EL PUNTO 3-------------------------------------
        ##--------------------------Cantidad de tarjetas débito maestro por segmento de clientes.
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\Crear_tablas\\punto_3.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
                    
            cursor.execute(contenido_sql)
            logging.info('[SUCCESS]: Se ha creado la tabla punto_3')
        except Exception as e:
            logging.error('[ERROR]: No se ha creado la tabla punto_3')

        ##------------------------------------------------------------------------------------------------------------------
        ## ------------------------INSERTAR LOS DATOS DEL PRIMER CURECE EN LA TABLA PUNTO_3 CREADA ANTERIORMENTE-------------
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\SQL3.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
            cursor.execute(contenido_sql)
            conn.commit()
            logging.info('[SUCCESS]: Se ha insertado el resultado del query SQL3 en la tabla punto_3')
        except Exception as e:
            logging.error('[ERROR]: No se ha insertado el resultado del query SQL3 en la tabla punto_3')

        logging.info('[SUCCESS]: Se ha ejecutado la tarea de las 8:00 AM')

    except Exception as e:
        logging.info('[ERROR]: No se ha ejecutado la tarea de las 8:00 AM')

schedule.every().day.at("00:00").do(tarea_programada_8)



##----------------------------------------------------------------------------------------------
### ----------------------------PROGRAMAR EJECUCIÓN A LAS 10:00 AM
##----------------------------------------------------------------------------------------------

def tarea_programada_10():
    try:
        ##------------------------------------------------------------------------------------------------------------------
        ## -----------------------------------CREAR TABLA EN MS ACCESS PARA EL PUNTO 4-------------------------------------
        ##------Las 10 cuentas activas con mayor cantidad de tarjetas activas asociadas organizado de menor a mayor.
        ##-----------------------------------------------------------------------------------------------------------------

        try: 
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\Crear_tablas\\punto_4.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
                    
            cursor.execute(contenido_sql)
            logging.info('[SUCCESS]: Se ha creado la tabla punto_4')
        except Exception as e:
            logging.error('[ERROR]: No se ha creado la tabla punto_4')



        ##------------------------------------------------------------------------------------------------------------------
        ## ------------------------INSERTAR LOS DATOS DEL PRIMER CURECE EN LA TABLA PUNTO_4 CREADA ANTERIORMENTE-------------
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\SQL4.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
            cursor.execute(contenido_sql)
            conn.commit()
            logging.info('[SUCCESS]: Se ha insertado el resultado del query SQL4 en la tabla punto_4')
        except Exception as e:
            logging.error('[ERROR]: No se ha insertado el resultado del query SQL4 en la tabla punto_4')

        ## -----------------------------------CREAR TABLA EN MS ACCESS PARA EL PUNTO 5-------------------------------------
        ##----------------------Cantidad de plásticos activos por cada tipo de tarjeta del portafolio de débito
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\Crear_tablas\\punto_5.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
                    
            cursor.execute(contenido_sql)
            logging.info('[SUCCESS]: Se ha creado la tabla punto_5')
        except Exception as e:
            logging.error('[ERROR]: No se ha creado la tabla punto_5')

        ##------------------------------------------------------------------------------------------------------------------
        ## ------------------------INSERTAR LOS DATOS DEL PRIMER CURECE EN LA TABLA PUNTO_5 CREADA ANTERIORMENTE-------------
        ##-----------------------------------------------------------------------------------------------------------------

        try:
            ruta_archivo_sql = 'C:\\Users\\dbarco\\Documents\\Prueba Tecnica DP 2\\Prueba-tecnica-DP-2\\SQL5.sql'
            contenido_sql = leer_archivos_sql(ruta_archivo_sql)
            cursor.execute(contenido_sql)
            conn.commit()
            logging.info('[SUCCESS]:Se ha insertado el resultado del query SQL5 en la tabla punto_5')
        except Exception as e:
            logging.error('[ERROR]: No se ha insertado el resultado del query SQL5 en la tabla punto_5')

            logging.info('[SUCCESS]: Se ha ejecutado la tarea de las 10:00 AM')

    except Exception as e:
        logging.info('[ERROR]: No se ha ejecutado la tarea de las 10:00 AM')

schedule.every().day.at("02:10").do(tarea_programada_10)

while True:
    schedule.run_pending()
    time.sleep(1)
