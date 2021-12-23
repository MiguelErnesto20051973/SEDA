from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion


def validarcampos():
    if ventana.txtNombre.text()=="" or ventana.txtCorreo.text() =="" :
        alerta=QMessageBox()
        alerta.setText('¡ Debes de llenar los campos ')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True


def agregar():
    if validarcampos():
        return False
    print("Hola soy la accion de agregar")
    nombre=ventana.txtNombre.text()
    correo=ventana.txtCorreo.text()
    print(nombre,correo)

    objContactos=conexion.contactos()
    contactos=objContactos.crearContacto((nombre,correo))
    consultar()

def eliminar():
    print("Hola soy la accion de eliminar")
    id= ventana.txtID.text()
    objContactos=conexion.contactos()
    contactos=objContactos.borrarContacto(id)

def modificar():
    if validarcampos():
        return False
    print("Hola soy la accion de modificar")
    id = ventana.txtID.text()
    nombre = ventana.txtNombre.text()
    correo = ventana.txtCorreo.text()
    print(nombre,correo)

    objContactos=conexion.contactos()
    contactos = objContactos.modificarContacto((nombre,correo,id))
    consultar()

def cancelar():
    print("Hola soy la accion de cancelar")
    consultar()

def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl = 0
    objContactos=conexion.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0,QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1,QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2,QTableWidgetItem(str(contacto[2])))
        indiceControl+=1

    ventana.txtID.setText("")
    ventana.txtNombre.setText("")
    ventana.txtCorreo.setText("")

    ventana.btnAgregar.setEnabled(True)
    ventana.bntEliminar.setEnabled(False)
    ventana.bntModificar.setEnabled(False)
    ventana.bntCancelar.setEnabled(False)

def seleccionar():
    id=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    correo=ventana.tblContactos.selectedIndexes()[2].data()
    print(id,nombre,correo)
    ventana.txtID.setText(id)
    ventana.txtNombre.setText(nombre)
    ventana.txtCorreo.setText(correo)

    ventana.btnAgregar.setEnabled(False)
    ventana.bntEliminar.setEnabled(True)
    ventana.bntModificar.setEnabled(True)
    ventana.bntCancelar.setEnabled(True)

aplicacion = QtWidgets.QApplication([])
ventana = uic.loadUi("ventana.ui")
ventana.show()
consultar()
ventana.tblContactos.setHorizontalHeaderLabels(['ID','Nombre','Correo'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect()

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())