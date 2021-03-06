#!/usr/bin/env python
# -*- encoding: utf8 -*-
# vim: ts=4

# Conference Chronometer está disponible bajo la Licencia Creative Commons
# "Atribución-No Comercial-Licenciar Igual 2.0 Chile". Puede encontrar una
# copia en http://creativecommons.org/licenses/by-nc-sa/2.0/cl/
# Autor: Renato M. Covarrubias Romero
# Email: rnt [at] rnt.cl
# URL  : http://rnt.cl/software/conference-chronometer/

# Modificado por: Emiliano P. Lopez
# Proyecto Forkeado en https://github.com/emilopez/Conference-Chronometer
# Email: emiliano.lopez [at] gmail.com

# ChangeLog
# Se cambió el uso original
# Ahora recibe 3 argumentos referidos a los minutos para cada color de fondo: verde, amarillo y rojo
# En función de estos valores cambia el color

import gtk
import gtk.gdk
import gobject
import sys
import pango


class Cronometro:
    '''
        Esta clase maneja el cronómetro.
        Cronómero de máximo 99 minutos con 59 segundos.
    '''


    def progress_timeout(self):
        '''
            Método usado como callback para modificar la barra de progreso.

            Llamado cada un segundo, actualiza:
            - El texto mostrado.
            - El tamaño de la barra.
            - El color de fondo de la barra.
            Al finalizar el tiempo, produce que el reloj se detenga y se
            muestre el botón para cerrar.
        '''

        self.tiempo+=1
        if self.tiempo > self.maxtiempo:
            return False

        self.pbar.set_text(self.formato % (str(self.tiempo/60).zfill(2), str(self.tiempo%60).zfill(2)))

        rel = float(self.tiempo)/float(self.maxtiempo)
        self.pbar.set_fraction(rel)

        if rel>(1-self.red_percent):
            self.pbar.modify_bg(gtk.STATE_SELECTED, gtk.gdk.color_parse("red") )
        elif rel>self.green_percent:
            self.pbar.modify_bg(gtk.STATE_SELECTED, gtk.gdk.color_parse("yellow") )
        else:
            self.pbar.modify_bg(gtk.STATE_SELECTED, gtk.gdk.color_parse("green") )
        return True

    def destroy_progress(self, widget, data=None):
        "	Se elimina el timer y se termina la aplicación."
		
        gobject.source_remove(self.timer)
        self.timer = 0
        gtk.main_quit()


    def __init__(self):
        """
            Contructor del objeto
            El primer argumento de entrada son los minutos a mostrar
        """

        green = float(sys.argv[1])
        yellow = float(sys.argv[2])
        red = float(sys.argv[3])
        tiempo_total = green + yellow + red
        		
        # Porcentajes
        self.green_percent = green/tiempo_total
        self.yellow_percent = yellow/tiempo_total
        self.red_percent = red/tiempo_total

        self.maxtiempo = tiempo_total*60
        self.tiempo = 0
        self.formato="%s:%s"

        # Creamos una ventana nueva
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)

        # Conectamos la acción 'destroy' al método 'destroy_progress'
        self.window.connect("destroy", self.destroy_progress)
        self.window.fullscreen()

        # Contenedor vertical: Barra de progreso y botón para Cerrar
        vbox = gtk.VBox(False, 2)
        vbox.set_border_width(1)
        self.window.add(vbox)
        vbox.show()

        # Creamos un objeto que siempre utilizará el tamaño máximo de la
        # ventana.
        align = gtk.Alignment(0, 0, 1, 1)
        vbox.pack_start(align)
        align.show()

        # Creamos la barra de progreso. Tipo de letra sans y tamaño 300.
        self.pbar = gtk.ProgressBar()
        self.pbar.set_text(self.formato % ("00", "00"))
        self.pbar.modify_font(pango.FontDescription("sans 300"))
        self.pbar.modify_fg(gtk.STATE_PRELIGHT, gtk.gdk.color_parse("black"))
        align.add(self.pbar)
        self.pbar.show()

        # Agregamos el callback para el timer que actualizará la barra de progreso.
        self.timer = gobject.timeout_add (1000, self.progress_timeout)

        # Agregamos el botón para salir del cronómetro
        self.button = gtk.Button("Cerrar")
        self.button.connect("clicked", self.destroy_progress)
        vbox.pack_start(self.button, False)

        # Esto hace que el botón sea el elemento por defecto
        self.button.set_flags(gtk.CAN_DEFAULT)

        # Presionando 'enter' se activa el botón.
        self.button.grab_default()
        self.button.show()

        # Mostramos la ventana
        self.window.show()


def isNumeric(s):
    "Retorna True si el dato ingresado es numérico."
    try:
        int(s)
        return True
    except:
        return False

def main():
    '''
        Función Inicial
        Realiza la validación de la entrada
    '''

    if len(sys.argv) == 4 and isNumeric(sys.argv[1]) and isNumeric(sys.argv[2]) and isNumeric(sys.argv[3]):
        Cronometro()
        gtk.main()
        return 0
    else:
        print "Use: %s <minutos_verde> <minutos_amarillo> <minutos_rojo>" % sys.argv[0]
        print "\nPara un cronómetro de 5 minutos: 2 verde, 2 amarillo y 1 rojo:"
        print "\t%s 2 2 1" % sys.argv[0]
        return 1


if __name__ == "__main__":
    main()
