import pyautogui, keyboard, time
#点击坐标数组
click_array = []
properties = []
is_running = False
with open('array.txt', 'r') as file:
    content = file.read()
    for item in content.split('\n'):
        click_array.append(item.split(','))

with open('hotKey.txt', 'r') as file:
    content = file.read()
    for item in content.split('\n'):
        properties.append(item)

key_start = properties[0]
key_stop = properties[1]
key_position = properties[2]
sleep_time = float(properties[3])

def logic_start():
    global is_running
    is_running = True
    print('已开启')

def logic_stop():
    global is_running
    is_running = False
    print('已暂停')

def logic_position():
    print(pyautogui.position())

# 按键事件监听
keyboard.add_hotkey(key_start, logic_start)
keyboard.add_hotkey(key_stop, logic_stop)
keyboard.add_hotkey(key_position, logic_position)

#任务执行
print('代码启动')
print('按下' + key_start + '开启运行')
print('按下' + key_stop + '暂停运行')
print('按下' + key_position + '获取鼠标坐标')
while True:
    if is_running:
        for num in click_array:
            pyautogui.click(num)
            time.sleep(sleep_time)
