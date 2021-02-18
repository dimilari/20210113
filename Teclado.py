import keyboard
from ctypes import windll
from time import sleep
import win32api


# leemos el carácter ingresado desde el teclado con la librería 'keyboard'
def pushed_key():
    return keyboard.read_key()
# determinamos el numero especial del idioma de entrada con la librería 'ctypes'
def language():
    user32 = windll.user32
    hwnd = user32.GetForegroundWindow()
    threadID = user32.GetWindowThreadProcessId(hwnd, None)
    StartLang = user32.GetKeyboardLayout(threadID)
    return StartLang

a = []
chars = 'aeioun?!AEIOUN'
spanish_chars = 'áéíóúñ¿¡ÁÉÍÓÚÑ'
while True:
    if language() == 67699721:
        win32api.LoadKeyboardLayout("00000409", 1)
        if len(pushed_key()) > 1:
            continue
        a.append(pushed_key())
        print(a, language())
        if a[-1] == '`' and a[0] in chars:
            ind = chars.find(a[0])
            keyboard.press('backspace')
            # pausa, usando la librería 'time'
            sleep(0.01)
            keyboard.press('backspace')
            keyboard.write(spanish_chars[ind])
        if len(a) >= 2:
            a = a[1:]


