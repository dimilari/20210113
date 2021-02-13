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

keyboard.start_recording()
keyboard.wait('a')
a = keyboard.stop_recording()
b = list(map(str, a))
c = ''
for i in b:
    if not 'up' in i and len(i) <= 21:
        c += (i[14:15])
print(c)


