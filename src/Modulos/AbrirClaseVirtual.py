from ..Acciones import eventos
Evento=eventos.Accion()

from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

class VerHorario:
    def Conectarse(self, driver):
        #Click en "Consulta Tu horario"
        Evento.WaitClickUntilVisible_Clikeable(driver,"/html/body/form/div[3]/div[3]/div[2]/div/div[2]/input")
        #se cambia a nueva pagina del horiario... falta codificar desde aquí...
