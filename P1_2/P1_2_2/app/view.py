# coding: utf-8
# sehr einfache Erzeugung des Markups f�r vollst�ndige Seiten
# jeweils 3 Abschnitte:
# - begin
# - content
# - end
# bei der Liste wird der content-Abschnitt wiederholt
# beim Formular nicht

import mako
import codecs
import os.path
import string
from mako import template
from mako.lookup import TemplateLookup

# ----------------------------------------------------------
class View_cl(object):
# ----------------------------------------------------------
	
	# -------------------------------------------------------
    def __init__(self):
    # -------------------------------------------------------
        pass
    
    # -------------------------------------------------------
    def createstart_px(self):
    # -------------------------------------------------------
        return self.readFile_p('index.html')
    
    # -------------------------------------------------------
    def createStudentList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['student']['list']
        template_o = template.Template(self.readTemplate_p('kunden_list.tpl'))
        return template_o.render(data_o = data_opl)           
    
    
    # -------------------------------------------------------
    def createLehrerList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['lehrer']['list']
        template_o = template.Template(self.readTemplate_p('lehrer_list.tpl'))
        return template_o.render(data_o = data_opl)  
    
    # -------------------------------------------------------
    def createFirmenList_px(self, data_opl):
    # -------------------------------------------------------
        data_opl = data_opl['firma']['list']
        template_o = template.Template(self.readTemplate_p('firma_list.tpl'))
        return template_o.render(data_o=data_opl)  
    
    # -------------------------------------------------------
    def createStudentForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('kunden_formform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl) 


    # -------------------------------------------------------
    def createLehrerForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('lehrerform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)     
    
    # -------------------------------------------------------
    def createFirmenForm_px(self, id_spl, data_opl):
    # -------------------------------------------------------
        # hier m�sste noch eine Fehlerbehandlung erg�nzt werden !
        template_o = template.Template(self.readTemplate_p('firmaform.tpl'))
        return template_o.render(data_o=data_opl, key_s = id_spl)
    
    # -------------------------------------------------------
    def readFile_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''

        with codecs.open(os.path.join('static', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
            
        return content_s
    
    # -------------------------------------------------------
    def readTemplate_p(self, fileName_spl):
    # -------------------------------------------------------   
        content_s = ''
    
        with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
                
        return content_s
    
        
# EOF
