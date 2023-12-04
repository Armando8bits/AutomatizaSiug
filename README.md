# AutomatizaSiug
Automatiza el inicio de sesión para clases virtuales de la universidad de Guayaquil

# Consideraciones
Este proyecto funciona con previa instación de los siguientes módulos:
pip install webdriver-manager
pip install PyAutoGUI
pip install python-dotenv
pip install selenium

Adicionalmente hay que configurar el archivo ".env" que almacenará las credenciales con la siguiente estructura:

usuar="cedula"
passw="contraseña"
fecme="04"
fecdi="06"
carre="TECNOLOGÍA DE LA INFORMACIÓN"
curso="2023 - 2024 CICLO 2"

Las comillas son recomendadas, este archivo puede estar grabado en la carpeta raiz, junto al arcivo Main.py

# Uso
Solo ejecute el archivo "Main.py" y la automatización entrará en funcionamiento con las credenciales configuradas previamente
o puedes crear un acceso directo del archivo antes mencionado para que este trabaje solo dandole doble click.