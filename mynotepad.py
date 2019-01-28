from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QWidget,QTextEdit,QMessageBox
from PyQt5.QtWidgets import QFileDialog,QFontDialog,QTextEdit
from PyQt5.QtPrintSupport import QPrinter,QPrintPreviewDialog
import sys

class window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title='MyNotepad'
        self.left=400
        self.top=200
        self.width=600
        self.height=400
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.page()
        self.editor()

    def editor(self):
        self.text = QTextEdit()
        self.setCentralWidget(self.text)

    def new(self):
        self.text.clear()

    def openfile(self):
        name ,_= QFileDialog.getOpenFileName(self)
        file= open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.text.setText(text)

    def savefile(self):
        name, _ = QFileDialog.getSaveFileName(self)
        file = open(name,'w')
        text = self.text.toPlainText()
        file.write(text)
        file.close()

    def printt(self):
        printer=QPrinter(QPrinter.HighResolution)
        dialog=QPrintPreviewDialog(printer,self)
        dialog.paintRequested.connect(self.printpreview)
        dialog.exec()

    def printpreview(self,printer):
            self.text.print_(printer)
        
 
    def cut(self):
        self.text.cut()
 
    def copy(self):
        self.text.copy()
 
    def paste(self):
        self.text.paste()

    def delete(self):
        self.text.clear()

    def undo(self):
        self.text.undo()
 
    def redo(self):
        self.text.redo()

    def clos(self):
        reply=QMessageBox.question(self,'Warning','Are you sure to close?',
                                   QMessageBox.Yes,QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.close()

    def font(self):
        font,ok=QFontDialog.getFont()

        if ok:
            self.text.setFont(font)

    

    def helpu(self):
        QMessageBox.about(self,"About","Notepad created by SOUMYA SEN")

        


    def page(self):

        menu=self.menuBar()
        file=menu.addMenu('File')
        edit=menu.addMenu('Edit')
        formt=menu.addMenu("Format")
        hel=menu.addMenu("Help")
    
        #file

        ##new
        new=QAction('New',self)
        new.setShortcut('Ctrl+n')
        new.triggered.connect(self.new)
        file.addAction(new)

        ##open
        ope=QAction('Open...',self)
        ope.setShortcut('Ctrl+o')
        ope.triggered.connect(self.openfile)
        file.addAction(ope)

        ##save
        sav=QAction('Save',self)
        sav.setShortcut('Ctrl+s')
        sav.triggered.connect(self.savefile)
        file.addAction(sav)

        ##print
        prin=QAction('Print',self)
        prin.setShortcut('Ctrl+p')
        prin.triggered.connect(self.printt)
        file.addAction(prin)

        ##exit
        ext=QAction('Exit',self)
        ext.setShortcut('Ctrl+d')
        ext.triggered.connect(self.clos)
        file.addAction(ext)


        #edit
        
        ##cut
        cut=QAction('Cut',self)
        cut.setShortcut('Ctrl+x')
        cut.triggered.connect(self.cut)
        edit.addAction(cut)

        ##copy
        copy=QAction('Copy',self)
        copy.setShortcut('Ctrl+c')
        copy.triggered.connect(self.copy)
        edit.addAction(copy)

        ##paste
        paste=QAction('Paste',self)
        paste.setShortcut('Ctrl+v')
        paste.triggered.connect(self.paste)
        edit.addAction(paste)

        ##delete
        delete=QAction('Delete',self)
        delete.setShortcut('del')
        delete.triggered.connect(self.delete)
        edit.addAction(delete)

        ##undo
        undo=QAction('Undo',self)
        undo.setShortcut('Ctrl+z')
        undo.triggered.connect(self.undo)
        edit.addAction(undo)

        ##redo
        redo=QAction('Redo',self)
        redo.setShortcut('Ctrl+y')
        redo.triggered.connect(self.redo)
        edit.addAction(redo)

        
        #format

        ##font
        fon=QAction('Font...',self)
        fon.setShortcut('Ctrl+f')
        fon.triggered.connect(self.font)
        formt.addAction(fon)
        
        #help
        helpp=QAction('About Notepad',self)
        helpp.triggered.connect(self.helpu)
        hel.addAction(helpp)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()


App=QApplication(sys.argv)
window1=window()
sys.exit(App.exec())
