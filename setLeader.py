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

2
3
	def buatComboBox(self):
		Label(self.frameAlarm, text='Jam : ').grid(row=0,column=0)
		self.alarmJam = StringVar()
		self.comboJam = Combobox(self.frameAlarm, textvariable=self.alarmJam,
                                state='readonly', width=2)
		self.comboJam['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                                     '16','17','18','19','20','21','22','23','24')
		self.comboJam.current(0)
		self.comboJam.grid(row=0,column=1)

		Label(self.frameAlarm, text='  Menit : ').grid(row=0,column=2)
		self.alarmMenit = StringVar()
		self.comboMenit = Combobox(self.frameAlarm, textvariable=self.alarmMenit,
                                state='readonly', width=2)
		self.comboMenit['values'] = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                                     '16','17','18','19','20','21','21','22','23','24','25','26','27','28','29','30',
                                     '31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46',
                                      '47','48','49','50','51','52','53','54','55','56','57','58','59')
		self.comboMenit.current(0)
		self.comboMenit.grid(row=0,column=3)

		self.frameAlarm.pack()

5