from ..Acciones import eventos
Evento=eventos.Accion()

from selenium.webdriver.support.ui import WebDriverWait #para esperar el elemento hasta que cargue
from selenium.webdriver.support import expected_conditions as EC #necesario para el de arriba
from selenium.webdriver.common.by import By #necesario para el de arriba

import time

class VerHorario:
    def Conectarse(self, driver, Carrera, Curso):
        Continuar=""
        while Continuar=="":
            #cierra modal del inicio
            #Evento.WaitClickUntilVisible_Clikeable(driver,"/html/body/form/div[3]/div[3]/div[1]/div/div/div[1]/button")
            Evento.WaitClickUntilVisible_ClikeableByClassName(driver,"close") #modifican la pagina con frecuencia, entonces es mejor buscarlo por classname
            #Click en "Consulta Tu horario"
            Evento.WaitClickUntilVisible_Clikeable(driver,"/html/body/form/div[3]/div[3]/div[2]/div/div[2]/input")
            #se cambia a nueva pagina del horiario... y
            #selecciona Carrera:
            Element=WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,"/html/body/form/div[3]/div[3]/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/select")))
            #Element.click()
            options = Element.find_elements(By.TAG_NAME, 'option')
            for option in options:
                if Carrera in option.text: #comprueba si el texto de cada elemento contiene la cadena
                    option.click()
                    break
            
            #espera que desaparezca el spinner
            WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]")))
            
            #selecciona Curso:
            Element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[3]/div[3]/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/select")))
            #Element.click()
            options = Element.find_elements(By.TAG_NAME, 'option')
            for option in options:
                if Curso in option.text: #comprueba si el texto de cada elemento contiene la cadena
                    option.click()
                    break

            #espera que desaparezca el spinner
            WebDriverWait(driver,90).until(EC.invisibility_of_element((By.XPATH,"/html/body/form/div[3]/div[3]/div[1]")))
            
            #click en boton "Clases Virtuales"
            driver.find_element(By.XPATH,"/html/body/form/div[3]/div[3]/div[2]/table/tbody/tr[4]/td[2]/div/div[1]/a").click()

            try:
                #esperar a que cargue la pagina (que encuentre el botón)
                Element = WebDriverWait(driver,90,1).until(EC.element_to_be_clickable((By.ID,"btnIrReunion")))
                url = Element.get_attribute('data-url') #obtengo el link del zoom meeting
                pos = url.find('?') #Encuentra la ubicación del '?'

                Element.click()
                print("****Link de Zoom: "+ url[:pos]) #imprime link hasta antes de '?'
                #espera que la pagina se cargue en su totalidad
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                #maneja el "OS App Selector" por teclado
                Evento.SetTab(driver,2) #toca tab 2 veces
                Evento.SetEnter(driver) #toca enter
                break #rompe el bucle si se llega a ejecutar hasta aqui
            except:
                Continuar=input("\n***Parece que no es hora de la clase, ¿Volver a Utilizar?\n\tPulse Enter para continuar...\n\tPulse cualquier letra seguido de enter para concluir...")
                if Continuar=="":
                    driver.back()
                    driver.back() #retrocede hacia atrás dos veces para iniciar nuevamente 
