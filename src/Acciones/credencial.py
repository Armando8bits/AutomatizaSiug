import os
import dotenv

class Credencial:
    usuari=""
    passwd=""
    fecme=""
    fecdi=""

    @classmethod
    def EsValida(cls):
        BoolEstado=True
        dotenv.load_dotenv()  # cargamos las variables de entorno
        cls.usuari = (os.getenv('usuar')) # leemos las varaibles de entorno
        cls.passwd = (os.getenv('passw'))
        cls.fecme = (os.getenv('fecme'))
        cls.fecdi = (os.getenv('fecdi'))
        if (cls.usuari is None or cls.passwd is None or cls.fecme is None or cls.fecdi is None):
            print("***CREDENCIALES INVALIDAS o INEXISTENTES")
            BoolEstado=False
        return BoolEstado
    
    @classmethod
    def GetUsuario(cls):
        return cls.usuari
    
    @classmethod
    def GetPasswor(cls):
        return cls.passwd
    
    @classmethod
    def GetFecdi(cls):
        return cls.fecdi
    
    @classmethod
    def GetFecme(cls):
        return cls.fecme
