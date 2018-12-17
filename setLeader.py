from tkinter import *
import time
from tkinter.ttk import Combobox
import pygame

class Jam:
    def __init__(self, parent):
        self.parent = parent
        self.frameAlarm = Frame(parent)

        self.hidupMati = BooleanVar(False)
        self.teksTombol = StringVar(value='set')

        self.fileMusik = 'Aisah.mp3'
        self.alarmHidup=False

        self.komponen()
        self.buatComboBox()
        self.buatTombol()
        self.perbaui()