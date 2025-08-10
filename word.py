import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction,
    QFileDialog, QFontComboBox, QComboBox, QToolBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class WordBenzeri(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Word Benzeri Metin Editörü")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #23272e;
                border-radius: 12px;
            }
            QTextEdit {
                background: #282c34;
                color: #f8f8f2;
                font-size: 17px;
                border-radius: 10px;
                padding: 12px;
                border: 1px solid #44475a;
            }
            QMenuBar {
                background: #23272e;
                color: #f8f8f2;
                font-size: 15px;
            }
            QMenuBar::item:selected {
                background: #44475a;
            }
            QToolBar {
                background: #23272e;
                border-bottom: 1px solid #44475a;
                spacing: 12px;
                padding: 8px;
            }
            QComboBox, QFontComboBox {
                background: #44475a;
                color: #f8f8f2;
                border-radius: 8px;
                padding: 6px 12px;
                min-width: 120px;
                font-size: 15px;
                border: 1px solid #6272a4;
            }
            QComboBox QAbstractItemView, QFontComboBox QAbstractItemView {
                background: #282c34;
                color: #f8f8f2;
                selection-background-color: #6272a4;
            }
        """)

        # Metin editörü
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Menü çubuğu
        self._menuOlustur()

        # Araç çubuğu
        self._toolbarOlustur()

    def _menuOlustur(self):
        menubar = self.menuBar()

        dosyaMenu = menubar.addMenu("Dosya")
        duzenMenu = menubar.addMenu("Düzen")

        yeniAction = QAction("Yeni", self)
        yeniAction.triggered.connect(self.yeniDosya)
        dosyaMenu.addAction(yeniAction)

        acAction = QAction("Aç", self)
        acAction.triggered.connect(self.dosyaAc)
        dosyaMenu.addAction(acAction)

        kaydetAction = QAction("Kaydet", self)
        kaydetAction.triggered.connect(self.dosyaKaydet)
        dosyaMenu.addAction(kaydetAction)

        cikisAction = QAction("Çıkış", self)
        cikisAction.triggered.connect(self.close)
        dosyaMenu.addAction(cikisAction)

        kesAction = QAction("Kes", self)
        kesAction.triggered.connect(self.textEdit.cut)
        duzenMenu.addAction(kesAction)

        kopyalaAction = QAction("Kopyala", self)
        kopyalaAction.triggered.connect(self.textEdit.copy)
        duzenMenu.addAction(kopyalaAction)

        yapistirAction = QAction("Yapıştır", self)
        yapistirAction.triggered.connect(self.textEdit.paste)
        duzenMenu.addAction(yapistirAction)

    def _toolbarOlustur(self):
        toolbar = QToolBar("Araç Çubuğu")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Yazı tipi seçimi
        self.fontBox = QFontComboBox()
        self.fontBox.currentFontChanged.connect(self.yaziTipiDegistir)
        toolbar.addWidget(self.fontBox)

        # Boyut seçimi
        self.fontSizeBox = QComboBox()
        self.fontSizeBox.setEditable(True)
        self.fontSizeBox.addItems([str(i) for i in range(8, 30, 2)])
        self.fontSizeBox.currentTextChanged.connect(self.yaziBoyutuDegistir)
        toolbar.addWidget(self.fontSizeBox)

    # Fonksiyonlar
    def yeniDosya(self):
        self.textEdit.clear()

    def dosyaAc(self):
        dosyaYolu, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt)")
        if dosyaYolu:
            with open(dosyaYolu, "r", encoding="utf-8") as f:
                self.textEdit.setText(f.read())

    def dosyaKaydet(self):
        dosyaYolu, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Metin Dosyaları (*.txt)")
        if dosyaYolu:
            with open(dosyaYolu, "w", encoding="utf-8") as f:
                f.write(self.textEdit.toPlainText())

    def yaziTipiDegistir(self, font):
        self.textEdit.setCurrentFont(font)

    def yaziBoyutuDegistir(self, size):
        if size.isdigit():
            self.textEdit.setFontPointSize(int(size))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = WordBenzeri()
    pencere.show()
    sys.exit(app.exec_())

