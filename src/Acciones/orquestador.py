from src.Modulos import AbrirClaseVirtual

class Orquestador:
    def Dirige(self, driver):
        AbrirClaseVirtual.VerHorario().Conectarse(driver)
