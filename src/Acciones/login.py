from ..Acciones import eventos
Evento=eventos.Accion()

from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba
from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc


class Sesion:
    def iniciar(self, driver,usuari,passwd,Fecme,Fecdi):
        #ingresa usuario
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/input")))\
            .send_keys(str(usuari))
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/input"))).send_keys(Keys.TAB)
        #ingresa contraseña
        Evento.WaitSendkeysUntilVisible_Clikeable(driver,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[2]/input",
            str(passwd) )
        #ingresa mes
        WebDriverWait(driver,30,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/input")))\
            .send_keys(str(Fecdi))
        #ingresa dia
        WebDriverWait(driver,30,2).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/input")))\
            .send_keys(str(Fecme))
        #baja la pagina para poder trabajar los controles:
        Evento.SetFlechaAbajo(driver) #baja la pagina 
        #da click en iniciar sesión
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]/div[3]/div/div/div/div/center/div/div[3]/div[1]/div[2]/div/div/div[2]/div[4]/input"))).click()

        #cierra modal del inicio
        Evento.WaitClickUntilVisible_Clikeable(driver,"/html/body/form/div[3]/div[3]/div[1]/div[2]/div/div[1]/button")