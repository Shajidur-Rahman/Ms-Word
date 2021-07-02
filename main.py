import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(20)
        self.font_box = QSpinBox()
        self.setWindowTitle("Ms Word")
        self.setWindowIcon(QtGui.QIcon('ms.png'))
        self.create_tool_bar()
        self.create_manu_bar()

    def create_manu_bar(self):
        manu_bar = QMenuBar()

        self.setMenuBar(manu_bar)

        file_manu = QMenu('File', self)
        manu_bar.addMenu(file_manu)

        save_as_pdf = QAction('Save as pdf', self)
        save_as_pdf.triggered.connect(self.save_as_pdf)
        file_manu.addAction(save_as_pdf)


        edit_manu = QMenu('Edit', self)
        manu_bar.addMenu(edit_manu)

        view_manu = QMenu('View', self)
        manu_bar.addMenu(view_manu)

    def create_tool_bar(self):
        tool_bar = QToolBar()

        undo_action = QAction( QtGui.QIcon('word/undo.png'), 'undo', self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action = QAction(QtGui.QIcon('word/redo.png'), 'redo', self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        cut_action = QAction(QtGui.QIcon('word/cut.png'), 'cut', self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        copy_action = QAction(QtGui.QIcon('word/copy.png'), 'copy', self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)

        paste_action = QAction(QtGui.QIcon('word/paste.png'), 'paste', self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()
        tool_bar.addSeparator()

        self.font_box.setValue(20)
        self.font_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_box)

        self.addToolBar(tool_bar)

    def set_font_size(self):
        value = self.font_box.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, 'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())