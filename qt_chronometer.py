# -*- encoding: utf8 -*-

#===============================================================================
# META
#===============================================================================

__version__ = "0.9.0"
__license__ = "GPL v3"
__author__ = "Emiliano López"
__email__ = "emiliano dot lopez at gmail dot com"
__url__ = "https://github.com/emilopez/Conference-Chronometer"
__date__ = "2014-09-16"

from ui import qt_chrono_class
import sys

def main():
    app = qt_chrono_class.nico.QtGui.QApplication(sys.argv)
    ventana = qt_chrono_class.chrono()
    ventana.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()