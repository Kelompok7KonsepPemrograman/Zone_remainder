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

        self.fileMusik = 'Tayo.mp3'
        self.alarmHidup=False

        self.komponen()
        self.buatComboBox()
        self.buatTombol()
        self.perbaui()

	def komponen(self):
		self.texsjam = stringvar()
		self.teks =label(teks="KELOMPOK7")
		self.teks.pack()
		
		layarjam = frame(self.parent,bd=10)
		layarjam.pack()
		
		self.jam = label(layar jam, texvariable=selg.teksjam,font=("hekvetica",40,'bold),bg ="light blue",fg="blue)
		self.jam.pack()
		
	def perbaui(self):
		datJam = time.strftime("%H:%M:%S", time.localtime())

		jam = time.strftime("%H", time.localtime())
		menit = time.strftime("%M", time.localtime())
		detik = time.strftime("%S", time.localtime())

		if jam==self.comboJam.get() and menit==self.comboMenit.get() and (detik=='00') and self.hidupMati.get() :
			pygame.init()
			pygame.mixer.init()
			pygame.mixer.music.load(self.fileMusik)
			pygame.mixer.music.play()
			self.alarmHidup=True

		if self.alarmHidup and pygame.mixer.music.get_busy()==False :
			self.perintahSetAlarm()

		self.teksJam.set(datJam)
		self.timer = self.parent.after(1000, self.perbaui)
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

	def buatTombol(self):
        self.tombolSet = Button(self.frameAlarm,textvariable=self.teksTombol,command=self.perintahSetAlarm).grid(row=0,column=4)

    def perintahSetAlarm(self):
        if self.teksTombol.get() == 'set' :
            self.teksTombol.set('stop')
            self.hidupMati.set(True)
            self.teks.config(text='Alarm Terpasang.!! pada -> '+ self.comboJam.get()+' : '+self.comboMenit.get() )
        else :
            self.hidupMati.set(False)
            self.teksTombol.set('set')
            self.alarmHidup=False
            try :
                pygame.mixer.music.stop()
            except :
                pass
            self.teks.config(text="KELOMPOK 7")

if __name__ == '__main__':
    root = Tk()
    root.title("Alarm")
    app = Jam(root)
    root.mainloop()