# Sistema de Gestión Informática — Veterinaria "La Bañera"

## Descripción del Proyecto

"La Bañera" es un sistema básico de gestión para una veterinaria, desarrollado en Python. 
Permite registrar clientes y sus mascotas, validar datos básicos, actualizar el peso, 
registrar atenciones clínicas, consultar el historial clínico y gestionar el 
agendamiento de citas médicas.

El proyecto utiliza Git y GitHub para el control de versiones e incorpora una práctica 
básica de integración continua mediante GitHub Actions y un Dockerfile para preparar 
un entorno reproducible de ejecución.

## Funcionalidades Principales

- Registro de clientes con nombre, documento y teléfono.
- Validación de clientes duplicados mediante el número de documento.
- Registro de mascotas asociadas a un cliente.
- Validación de nombre y raza de la mascota.
- Validación de edad y peso mediante valores mayores que cero.
- Consulta y listado de mascotas registradas.
- Actualización del peso de una mascota.
- Registro de atenciones clínicas mediante motivo y diagnóstico.
- Consulta del historial clínico de una mascota.
- Agendamiento de citas indicando mascota, fecha y hora.
- Consulta y listado de las citas agendadas.

## Requerimientos Funcionales Implementados

- **RF-01 y RF-02:** Registro de mascotas y validación de los datos numéricos de edad y peso.
- **RF-03:** Actualización del peso de las mascotas.
- **RF-04:** Registro y consulta del historial de atenciones clínicas.
- **RF-05 y RF-06:** Registro de clientes y asociación de mascotas con sus respectivos dueños.
- **RF-07 y RF-09:** Registro y consulta de citas médicas.

## Requisitos No Funcionales

- **RNF-01 (Rendimiento):** El sistema permite realizar consultas del historial clínico mediante 
  estructuras de datos en memoria.
- **RNF-02 (Seguridad):** No se implementa control de acceso mediante roles en la versión actual 
  del sistema.

## Integración Continua

El proyecto incorpora un flujo básico de Integración Continua mediante GitHub Actions.

Después de cada envío de cambios (`push`) a las ramas configuradas, GitHub ejecuta 
automáticamente una validación de sintaxis del código Python mediante:

```bash
python -m py_compile Taller8.py
##  Autor
* **Desarrollador / Ingeniero en curso:** Fernando (Proyecto Académico - Metodologías y Requerimientos de Software).
Prueba de integración continua solo prueba de cambio de git.