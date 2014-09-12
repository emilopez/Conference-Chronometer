from ui import qt_chrono_class
import sys

def main():
    app = qt_chrono_class.nico.QtGui.QApplication(sys.argv)
    ventana = qt_chrono_class.chrono()
    ventana.show()
    sys.exit(app.exec_())

if __name__== '__main__':
    main()