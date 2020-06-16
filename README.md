# Python Examples.
## Flask
Aquí tenemos los ejemplos básicos sobre como crear servidores en Flask de una forma sencilla.

* flask1
    Muestra de una forma muy sencilla como implementar un endpoint con un get básico. 
    Nos enseña a crear la estructura más básica posible.
    Tiene dos endpoint get, uno con parámetro y otro sin parámetro.
    Podemos observar la forma en la que devuelve la respuesta en formato json.


##Concurrency
### ThreadPoolExecutor
Es un ejemplo muy básico de como hacer peticiones concurrentes haciendo uso de : ThreadPoolExecutor

Hace uso de un servicio REST básico de ejemplo que está en la sección de Flask (get)

Consta de 4 ficheros donde vemos la refactorización desde el principio sin ejecución concurrente hasta llegar al ejemplo final

* main_1.py
    Ejemplo de como hacer una petición get.

* main_2.py
    Modificación del fichero anterior, donde creamos un conjunto de datos muy rápido.
    
* main_3.py
    Refactorización del anterior que nos permite tener una mejor visión de la estructura del código.
   
* main_4.py
    En este ejemplo implementamos la llamada de forma concurrente con el ThreadPoolExecutor

