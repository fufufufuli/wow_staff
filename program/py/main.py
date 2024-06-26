import pyautogui, keyboard, time

array = []
properties = []
is_running = False
with open('array.txt', 'r') as file:
    content = file.read()
    for item in content.split('\n'):
        array.append(item.split(','))

with open('hotKey.txt', 'r') as file:
    content = file.read()
    for item in content.split('\n'):
        properties.append(item)

start = properties[0]
stop = properties[1]
position = properties[2]
calc = float(properties[3])


def start_logic():
    global is_running
    is_running = True
    print('已开启')


def stop_logic():
    global is_running
    is_running = False
    print('已暂停')


def position_logic():
    print(pyautogui.position())


# 按键事件处理

keyboard.add_hotkey(start, start_logic)
keyboard.add_hotkey(stop, stop_logic)
keyboard.add_hotkey(position, position_logic)
print('代码启动')
print('按下' + start + '开启运行')
print('按下' + stop + '暂停运行')
print('按下' + position + '获取鼠标坐标')
while True:
    if is_running:
        for num in array:
            pyautogui.click(num)
            time.sleep(calc)
