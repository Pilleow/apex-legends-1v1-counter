from pynput import keyboard
from playsound import playsound
from os import system

points = [0, 0]
names = ["Player 1", "Player 2"]
spaces = ["", ""]
last_points = points.copy()

def update_view():
    system("cls")
    print(f"#\n#  {spaces[0]}{names[0]}: {points[0]}\n#\n#  {spaces[1]}{names[1]}: {points[1]}\n#\n")

def on_press(key):
    global points, last_points

    if key == keyboard.Key.left:
        playsound('sounds/point_1.wav', False)
        last_points = points.copy()
        points[0] += 1
        update_view()

    elif key == keyboard.Key.right:
        playsound('sounds/point_2.wav', False)
        last_points = points.copy()
        points[1] += 1
        update_view()

    elif key == keyboard.Key.down and last_points != points:
        playsound('sounds/revert.wav', False)
        points = last_points.copy()
        update_view()

names[0] = input("#\n#   First player: ")
names[1] = input("#\n#  Second player: ")
spaces[0] = "".join([" " for _ in range(abs(len(names[0]) - len(names[1])))])
if len(names[0]) > len(names[1]):
    spaces.reverse()

update_view()
print("\n#  Use LEFT / RIGHT arrows to add points.\n#  Click DOWN arrow to undo an action.\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()