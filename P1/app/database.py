# coding: utf-8
import os 
import os.path 
import codecs
import json
#---------------------------------------------------------
class Database_cl(object): 
#---------------------------------------------------------
    # da es hier nur darum geht, die Daten dauerhaft zu speichern,
    # wird ein sehr einfacher Ansatz verwendet: 
    # - es können Daten zu genau 15 Teams gespeichert werden 
    # - je Team werden 2 Teilnehmer mit Namen, Vornamen und Matrikelnummer 
    #   berücksichtigt 
    #   SOWIE ALS Ergänzung: Semesterzahl! 
    # - die Daten werden als eine JSON-Datei abgelegt
    
    #------------------------------------------------------
    def __init__(self): 
    #------------------------------------------------------
        self.data_o = None 
        self.readData_p()
    #------------------------------------------------------
    
    def create_px(self, data_opl): 
    #------------------------------------------------------
        # Überprüfung der Daten müsste ergänzt werden!
        # 'freien' Platz suchen, 
        # falls vorhanden: belegen und Nummer des Platzes als Id zurückgeben
        id_s = None 
        for loop_i in range(0,15): 
            if self.data_o[str(loop_i)][0] == '': 
                id_s = str(loop_i) 
                self.data_o[id_s] = data_opl 
                self.saveData_p() 
                break
        return id_s
    #------------------------------------------------------
    def read_px(self, id_spl = None): 
    #------------------------------------------------------
        # hier zur Vereinfachung: 
        # Aufruf ohne id: alle Einträge liefern 
        data_o = None 
        if id_spl == None: 
            data_o = self.data_o 
        else: 
            if id_spl in self.data_o: 
                data_o = self.data_o[id_spl]
        return data_o
    
    #------------------------------------------------------
    
    def update_px(self, id_spl, data_opl):
    #------------------------------------------------------
    # Überprüfung der Daten müsste ergänzt werden! 
        status_b = False 
        if id_spl in self.data_o: 
            self.data_o[id_spl] = data_opl 
            self.saveData_p() 
            status_b = True
        return status_b
    
    #------------------------------------------------------
    
    def delete_px(self, id_spl): 
    #------------------------------------------------------
        status_b = False 
        if id_spl in self.data_o: 
            pass 
            # hier müssen Sie den Code ergänzen 
            # Löschen als Zurücksetzen auf die Default-Werte implementieren
            self.data_o[id_spl] = self.getDefault_px()
            self.saveData_p()
            status_b = True
            
            
            # Ihre Ergänzung
        return status_b
    #------------------------------------------------------
    def getDefault_px(self): 
    #------------------------------------------------------
        return ['', '', '', '', ''] # HIER müssen Sie eine Ergänzung vornehmen -> erl
        
    #------------------------------------------------------
    def readData_p(self): 
        #------------------------------------------------------
        try: 
            fp_o = codecs.open(os.path.join('data', 'webteams.json'), 'r', 'utf-8') 
        except: 
            # Datei neu anlegen 
            self.data_o = {} 
            for loop_i in range(0,15): 
                self.data_o[str(loop_i)] = ['', '', '', '', '']  # HIER müssen Sie eine Ergänzung vornehmen -> erl
                self.saveData_p() 
        else: 
            with fp_o: 
                self.data_o = json.load(fp_o)
        return
    #------------------------------------------------------
    
    def saveData_p(self): 
        #------------------------------------------------------
        with codecs.open(os.path.join('data', 'webteams.json'), 'w', 'utf-8') as fp_o: 
            json.dump(self.data_o, fp_o)
# EOF

