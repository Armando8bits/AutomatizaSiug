from src.Modulos.Contratos import contratoReg
from src.Modulos.Afiliaciones import afiliacionReg, afiliacionEdit

class Orquestador:
    def Dirige(self, driver):
        #contratoReg.Contrato().Registrar(driver)
        #afiliacionReg.Afiliacion().Registrar(driver)
        afiliacionEdit.Afiliacion().Editar(driver)
