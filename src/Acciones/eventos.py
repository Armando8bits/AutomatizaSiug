from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

from selenium.webdriver.common.action_chains import ActionChains #para manejar dobleClik
from selenium.webdriver.common.keys import Keys  #para enviar teclas como ENTER, ESC, etc
from selenium.webdriver.common.action_chains import ActionChains #para usar teclado directamente en driver y usar bajar pagina y etc

class Accion:
        def WaitSendkeysUntilVisible_Clikeable(self,driver,strXXpath,Teclas):
            elements= WebDriverWait(driver,90,1).until(
                EC.all_of(
                EC.visibility_of_element_located((By.XPATH,strXXpath))
                ,
                EC.element_to_be_clickable((By.XPATH,strXXpath))
                )
                )
            elements[0].send_keys(Teclas)

        def SetAVPAG(self, driver, Nveces=1):
            '''Pulsa la tecla AV.PAG un numero de veces configuradas'''
            actions = ActionChains(driver)
            for i in range(1, Nveces + 1):
                actions.send_keys(Keys.PAGE_DOWN).perform()

        def SetFlechaAbajo(self, driver, Nveces=1):
            '''Pulsa la tecla FLECHA_ABAJO un numero de veces configuradas'''
            actions = ActionChains(driver)
            for i in range(1, Nveces + 1):
                actions.send_keys(Keys.ARROW_DOWN).perform()
        
        def WaitClickUntilVisible_ClikeableByClassName(self,driver,strClassName):
            elements= WebDriverWait(driver,90,1).until(
                EC.all_of(
                EC.visibility_of_element_located((By.CLASS_NAME,strClassName))
                ,
                EC.element_to_be_clickable((By.CLASS_NAME,strClassName))
                )
                )
            elements[0].click()
        
        def WaitClickUntilVisible_Clikeable(self,driver,strXXpath):
            elements= WebDriverWait(driver,90,1).until(
                EC.all_of(
                EC.visibility_of_element_located((By.XPATH,strXXpath))
                ,
                EC.element_to_be_clickable((By.XPATH,strXXpath))
                )
                )
            elements[0].click()