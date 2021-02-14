import keyboard
import time
# keyboard.wait('a')
# keyboard.write('á')

# a = keyboard.read_hotkey()
# b = keyboard.read_key()

# keyboard.start_recording()
# keyboard.wait('enter')
# keyboard.stop_recording()
# keyboard.record(until='enter')

# a = keyboard.record(until='enter')
# keyboard.play(a)

# keyboard.add_word_listener('aa', func, 'a')
# keyboard.wait('enter')

# a = keyboard.record(until='enter')
# print(a)
# keyboard.press('backspace down')
# KeyboardEvent(backspace down), KeyboardEvent(backspace up)


########## keyboard.press(('backspace', 'backspace','backspace'))

# a = keyboard.read_key()
# print(a)

while True:
    keyboard.start_recording()
    keyboard.wait('`')
    source_line = keyboard.stop_recording()
    list_line = list(map(str, source_line))
    c = ''
    for i in list_line:
        if not 'up' in i and len(i) <= 21:
            c += (i[14:15])
    print(c)
    chars = 'aeioun?!'
    spanish_chars = 'áéíóúñ¿¡'
    if c[-2] in chars:
        keyboard.press(('backspace', 'backspace'))
        ind = chars.find(c[-2])
        keyboard.write(spanish_chars[ind])
