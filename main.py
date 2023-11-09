from src.Acciones import login, credencial
#from login import Sesion
from src.Acciones import orquestador

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService #para no estar descargando el chromedriver
from webdriver_manager.chrome import ChromeDriverManager

if credencial.Credencial.EsValida(): #si las credenciales son validas, inicia
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-default-apps")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window() #creo que es obvio lo que hace
    driver.get("https://servicioenlinea.ug.edu.ec/SIUG/Account/Login.aspx")

    login.Sesion().iniciar(driver,credencial.Credencial.GetUsuario(),
                           credencial.Credencial.GetPasswor(),
                           credencial.Credencial.GetFecme(),
                           credencial.Credencial.GetFecdi()     )
    orquestador.Orquestador().Dirige(driver)
    input("***Presiona ENTER para cerrar el navegador...") #para evitar que se cierre al culminar el script
    driver.quit()



