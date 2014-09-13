Conference-Chronometer
======================

Proyecto derivado de https://github.com/rnt/Conference-Chronometer que agrega funcionalidades e interfaz gráfica.

Descripción
-----------

Cronómetro para conferencias que muestra el tiempo de transcurre y cambia el color de fondo entre verde, amarillo y rojo según la configuración del usuario. Para una charla es de 15 minutos uno puede configurar el cronómetro para que muestre un determinado tiempo cada color (5,5,5 o 1,9,5, etc, etc, etc). 

El tiempo total del cronómetro es la suma de los tiempos ingresados en cada color. Si una charla es de 15 minutos, mas 5 de preguntas, se debe tener en cuenta de sumar este tiempo según como sea necesario.

La interfaz gráfica es muy intuitiva, permite guardar distintos tipos de cronómetros, para ser ejecutados según la necesidad. Podría guardar una charla de 15 minutos con una determinada configuración y otra, por ejemplo con otro nombre y configuración. Usualmente en las conferencias hay disitntos tipos de charlas, oradores, charlas magistrales, etc, cada una con su tiempo. 

Existen dos maneras de ejecutar el cronómetro:

Desde la consola
----------------

El cronómetro se ejecuta con tres argumentos donde cada uno es el tiempo del color de la barra de progreso. Por ejemplo para que el tiempo por color sea 1 minuto verde, 2 minutos amarillo y 3 minutos rojo se lo debe ejecutar del siguiente modo:

    ./chronometer.py 1 2 3

Con la ejecución previa el tiempo total sería de 6 minutos.

Desde la interfaz gráfica
-------------------------

Ejecute qt_chronometer.py y luego:

* Cargue el cronómetro en la lista ingresando el tiempo por cada color y presionado Save
* Ejecute el cronómetro haciendo doble click sobre un item de la lista o seleccionándolo y presionando Launch Timer


To do
-----

* Agregar menú con ayuda y acerca de  
* Título a lista de cronómetros
* Empaquetar
