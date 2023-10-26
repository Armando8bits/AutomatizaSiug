from src.Modulos import AbrirClaseVirtual
from src.Acciones import credencial

class Orquestador:
    def Dirige(self, driver):
        AbrirClaseVirtual.VerHorario().Conectarse(driver,
                                                  credencial.Credencial.GetCarre(), #carrera
                               credencial.Credencial.GetCurso()  #Curso
        )         
