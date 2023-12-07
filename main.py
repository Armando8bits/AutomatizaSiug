from src.Acciones import login, credencial
#from login import Sesion
from src.Acciones import orquestador

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #para no estar descargando el chromedriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

if credencial.Credencial.EsValida(): #si las credenciales son validas, inicia
    options = Options()
    options.add_argument("--incognito")
    '''El perfil de Chrome "Incognito" no verifica los certificados SSL por defecto. Esta opción es más segura que la anterior,
    ya que el perfil de incognito no guarda cookies ni historial de navegación. en lugar de usar el argumento "--ignore-certificate-errors"
    al inicio de Chrome, lo que le indicará que ignore cualquier error relacionado con los certificados SSL. pero este último no es recomendado
    ya que una práctica insegura y no se recomienda, ya que expone su conexión a posibles ataques y robo de datos. '''
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window() #creo que es obvio lo que hace
    driver.get("https://servicioenlinea.ug.edu.ec/SIUG/Account/Login.aspx")

    login.Sesion().iniciar(driver,credencial.Credencial.GetUsuario(),
                           credencial.Credencial.GetPasswor(),
                           credencial.Credencial.GetFecme(),
                           credencial.Credencial.GetFecdi()     )
    orquestador.Orquestador().Dirige(driver)
    input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script
    driver.quit()



