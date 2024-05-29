from ..Acciones import eventos
Evento=eventos.Accion()

import time
from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba
from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc


class Sesion:
    def iniciar(self, driver,usuari,passwd,Fecme,Fecdi):
        #ingresa usuario
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID ,"MainContent_LoginUser_UserName")))\
            .send_keys(str(usuari))
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"MainContent_LoginUser_UserName"))).send_keys(Keys.TAB)
        #ingresa contraseña
        time.sleep(0.5)
        Evento.WaitSendkeysUntilVisible_Clikeable_id(driver,"MainContent_LoginUser_Password",
            str(passwd) )
        #ingresa mes
        WebDriverWait(driver,30,2).until(EC.element_to_be_clickable((By.ID,"MainContent_LoginUser_TXT_MES")))\
            .send_keys(str(Fecdi))
        #ingresa dia
        WebDriverWait(driver,30,2).until(EC.element_to_be_clickable((By.ID,"MainContent_LoginUser_TXT_DIA")))\
            .send_keys(str(Fecme))
        #baja la pagina para poder trabajar los controles:
        Evento.SetFlechaAbajo(driver) #baja la pagina 
        #da click en iniciar sesión
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"MainContent_LoginUser_LoginButton"))).click()