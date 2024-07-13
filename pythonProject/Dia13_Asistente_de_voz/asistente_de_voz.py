'''
requirements.txt
# Si da error:
# from distutils import LooseVersion
# ModuleNotFoundError: No module named 'distutils'     
# Instalar: 
    python -m ensurepip --upgrade
    pip install setuptools
flask
speech_recognition #pip3 install speechrecognition
pyttsx3
pywhatkit
pipwin
PyAudio
wikipedia
yfinance
pyjokes
'''
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import wikipedia
import webbrowser
import datetime

# Escuchar nuestro micrófono
def transformar_audio_en_texto():
    r = sr.Recognizer()
    print('Iniciando, un momento por favor...')
    # Configurar el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera para escuchar
        r.pause_threshold = 0.8
        print("Puedes empezar a hablar...")
        r.adjust_for_ambient_noise(origen, duration=1)
        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en Google
            tu_audio = r.recognize_google(audio, language="es-ES")
            # Prueba de que se reconoció el audio
            print("Entendido: " + tu_audio)            
            print("Audio reconocido")
            return tu_audio
        except sr.UnknownValueError:
            # No se reconoció el audio
            print("No se reconoció el audio")
            return "Intentalo nuevamente"
        # En caso de que no se reconozca el audio
        except sr.RequestError:
            print(f"Error al buscar en Google")
            return "Intentalo nuevamente"
        # Error inesperado
        except:
            print(f"Error inesperado")
            return "Intentalo nuevamente"

def hablar(texto):
    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()
    # Velocidad de la voz
    engine.setProperty('rate', 160)
    # Volumen de la voz
    engine.setProperty('volume', 0.4)
    # Configurar el lenguaje de la voz
    voices = engine.getProperty('voices')
    # Se escoge la voz de la lista instalada en Windows
    engine.setProperty('voice', voices[0].id)
    # Texto a hablar
    engine.say(texto)
    # Ejecutar la voz
    engine.runAndWait()

# Decir que día de la semana es.
def decir_dia():
    # Crear variable para la fecha actual
    fecha = datetime.datetime.now()
    # Día de hoy
    dia = datetime.date.today()
    print("Hoy es " + str(dia))

    # Crear día de la semana
    dia_semana = dia.weekday()
    print("Día de la semana: " + str(dia_semana))

    # Diccionario de los días de la semana
    dias_semana = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

    # Decir día de la semana
    hablar("Hoy es " + dias_semana[dia_semana])

# Decir la hora actual
def decir_hora():
    # Crear variable para la fecha actual
    fecha = datetime.datetime.now()
    # Hora actual
    hora = fecha.hour
    minuto = fecha.minute
    print("Son las " + str(hora) + ":" + str(minuto))

    # Decir la hora
    if hora == 1:
        hablar("Es la una")
    elif (hora > 1 and hora < 2):
        hablar("Es la " + str(hora) + " y" + str(minuto) + " minutos")
    else:
        hablar("Son las " + str(hora) + " y " + str(minuto) + " minutos")

# Función saludo inicial
def decir_saludo():
    # Crear variable para la fecha actual
    fecha = datetime.datetime.now()
    # Hora actual
    hora = fecha.hour
    # Saludo inicial
    if hora > 6 and hora < 12:
        momento = "Buenos días."
    elif hora >= 12 and hora < 18:
        momento = "Buenas tardes."
    else:
        momento = "Buenas noches."
    hablar(f'{momento}, soy Helena, ¿En qué te puedo ayudar?')

# Función principal
def pedir_cosas_al_asistente():
    decir_saludo()
    while True:
        # Escuchar el audio
        audio = transformar_audio_en_texto().lower()
        # Salir del programa
        if "chao" in audio:
            hablar("Un placer haberte ayudado, hasta la próxima")
            break
        # Decir la hora
        elif "qué hora es" in audio:
            decir_hora()
            continue
        # Decir el día de la semana
        elif "qué día es hoy" in audio:
            decir_dia()
            continue
        # abrir google
        elif "abrir google" in audio:
            hablar("Abriendo Google")
            webbrowser.open("https://google.com")
            continue
        # Buscar en Wikipedia
        elif "busca en wikipedia" in audio:
            hablar("Buscando en wikipedia")
            audio = audio.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(audio, sentences=1)
            #print(resultado)
            hablar(f'Wikipedia dice lo siguiente: {resultado}')
            continue
        # Buscar en Yahoo Finance
        elif "busca en yahoo finance" in audio:
            audio = audio.replace("busca en yahoo finance", "")
            busqueda = transformar_audio_en_texto()
            resultado = yf.Ticker(busqueda).info
            #print(resultado)
            hablar(resultado)
            continue
        # Buscar en Google
        elif "busca en internet" in audio:
            audio = audio.replace("busca en internet", "")
            busqueda = transformar_audio_en_texto()
            pywhatkit.search(busqueda)
            continue
        # Abrir YouTube
        elif "reproducir en youtube" in audio:
            hablar("Buena elección, reproduciendo en Youtube")
            audio = audio.replace("reproducir en youtube", "")
            pywhatkit.playonyt(audio)
            break
        # Jokes
        elif "chiste" in audio:
            hablar("Espero que te guste el chiste.")
            hablar(pyjokes.get_joke('es'))            
            continue
        # No entiendo
        else:
            hablar("No te he entendido, puedes repetirlo")

pedir_cosas_al_asistente()
