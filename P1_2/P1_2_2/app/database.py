# coding: utf-8
import os
import os.path
import codecs
import json
import datetime
#----------------------------------------------------------
class Database_cl(object):
#----------------------------------------------------------
# da es hier nur darum geht, die Daten dauerhaft zu speichern,
# wird ein sehr einfacher Ansatz verwendet:
# - es k�nnen Daten zu genau 15 Teams gespeichert werden
# - je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer
# ber�cksichtigt
# - die Daten werden als eine JSON-Datei abgelegt
	
	#-------------------------------------------------------
	def __init__(self):
	#-------------------------------------------------------
		self.data_o = None
	
	#-------------------------------------------------------
	def readStudent_px(self, id_spl):
	#-------------------------------------------------------
		# hier zur Vereinfachung:
		# Aufruf ohne id: alle Eintr�ge liefern
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['student']['list'][id_spl]
			
		return data_opl
	
	#-------------------------------------------------------
	def readLehrer_px(self, id_spl):
	#-------------------------------------------------------
		# hier zur Vereinfachung:
		# Aufruf ohne id: alle Eintr�ge liefern
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['lehrer']['list'][id_spl]
				
		return data_opl
	
	#-------------------------------------------------------
	def readFirma_px(self, id_spl):
	#-------------------------------------------------------
		# hier zur Vereinfachung:
		# Aufruf ohne id: alle Eintr�ge liefern
		data_opl = None
		if id_spl != None:
			data_opl = self.data_o['firma']['list'][id_spl]
				
		return data_opl
	
	#-------------------------------------------------------
	def updateStudent_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['student']['list'][id_spl] = data_opl
		self.saveData_p()
		return 
	
	#-------------------------------------------------------
	def updateLehrer_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['lehrer']['list'][id_spl] = data_opl
		self.saveData_p()
		return
	
	#-------------------------------------------------------
	def updateFirma_px(self, id_spl, data_opl):
	#-------------------------------------------------------
		self.data_o['firma']['list'][id_spl] = data_opl
		self.saveData_p()
		return
	
	#-------------------------------------------------------
	def createStudent_px(self, data_opl):
	#-----------------------------------------------------
		self.data_o['student']['list'].update({self.data_o['student']['count']: ''})
		self.data_o['student']['list'][self.data_o['student']['count']] = data_opl
		self.data_o['student']['count'] += 1
		self.saveData_p();
		return 
	
	#-------------------------------------------------------
	def createLehrer_px(self, data_opl):
	#-------------------------------------------------------
		self.data_o['lehrer']['list'].update({self.data_o['lehrer']['count']: ''})
		self.data_o['lehrer']['list'][self.data_o['lehrer']['count']] = data_opl
		self.data_o['lehrer']['count'] += 1
		self.saveData_p();
		return	
	
	#-------------------------------------------------------
	def createFirma_px(self, data_opl):
	#-------------------------------------------------------
		self.data_o['firma']['list'].update({self.data_o['firma']['count']: ''})
		self.data_o['firma']['list'][self.data_o['firma']['count']] = data_opl
		self.data_o['firma']['count'] += 1
		self.saveData_p();
		return
		
	#-------------------------------------------------------	
	def deleteStudent_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['student']['list'][id_spl]
		self.saveData_p()

		return
	
	#-------------------------------------------------------	
	def deleteLehrer_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['lehrer']['list'][id_spl]
		self.saveData_p()

		return	

	#-------------------------------------------------------	
	def deleteFirma_px(self, id_spl):
	#-------------------------------------------------------
		del self.data_o['firma']['list'][id_spl]
		self.saveData_p()

		return
	
	#-------------------------------------------------------
	def readData_p(self):
	#-------------------------------------------------------
		fp_o = codecs.open(os.path.join('data', 'ppm.json'), 'r', 'utf-8')
		with fp_o:
			self.data_o = json.load(fp_o)
			
		for key in range(0, len(self.data_o['ppaktuell']['list'])):	
			anfangsdatum = self.data_o['ppaktuell']['list'][key]['anfangsdatum'].split('.')
			self.data_o['ppaktuell']['list'][key]['anfangsdatum'] = datetime.date(int(anfangsdatum[2]), int(anfangsdatum[1]), int(anfangsdatum[0]))
			
			enddatum = self.data_o['ppaktuell']['list'][key]['enddatum'].split('.')
			self.data_o['ppaktuell']['list'][key]['enddatum'] = datetime.date(int(enddatum[2]),int(enddatum[1]),int(enddatum[0]))
			
		for key in range(0, len(self.data_o['ppabgeschlossen']['list'])):	
			anfangsdatum = self.data_o['ppabgeschlossen']['list'][key]['anfangsdatum'].split('.')
			self.data_o['ppabgeschlossen']['list'][key]['anfangsdatum'] = datetime.date(int(anfangsdatum[2]),int(anfangsdatum[1]),int(anfangsdatum[0]))
						
			enddatum = self.data_o['ppabgeschlossen']['list'][key]['enddatum'].split('.')
			self.data_o['ppabgeschlossen']['list'][key]['enddatum'] = datetime.date(int(enddatum[2]),int(enddatum[1]),int(enddatum[0]))
		
		return self.data_o
	
	#-------------------------------------------------------
	def saveData_p(self):
	#-------------------------------------------------------
		for key in range(0, len(self.data_o['ppaktuell']['list'])):
			self.data_o['ppaktuell']['list'][key]['anfangsdatum'] = self.data_o['ppaktuell']['list'][key]['anfangsdatum'].strftime('%d.%m.%Y')
			self.data_o['ppaktuell']['list'][key]['enddatum'] = self.data_o['ppaktuell']['list'][key]['enddatum'].strftime('%d.%m.%Y')
			
		for key in range(0, len(self.data_o['ppabgeschlossen']['list'])):
			self.data_o['ppabgeschlossen']['list'][key]['anfangsdatum'] = self.data_o['ppabgeschlossen']['list'][key]['anfangsdatum'].strftime('%d.%m.%Y')
			self.data_o['ppabgeschlossen']['list'][key]['enddatum'] = self.data_o['ppabgeschlossen']['list'][key]['enddatum'].strftime('%d.%m.%Y')		
			
			
		with codecs.open(os.path.join('data', 'ppm.json'), 'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)
# EOF
