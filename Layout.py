# -*- coding: UTF-8 -*-
# Layout.py
from PyQt5.QtGui import QPalette, QColor, QFont

class CustomPalette:
    @staticmethod
    def set_dark_palette(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))  # Schwarzer Hintergrund
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # Wei�e Schrift
        palette.setColor(QPalette.Base, QColor(0, 0, 255))  # Blauer Hintergrund f�r Textbox
         # Setzen Sie die Schriftart auf Helvetica, Gr��e 24
        font = QFont("Helvetica", 24)
        app.setFont(font)
        app.setPalette(palette)

