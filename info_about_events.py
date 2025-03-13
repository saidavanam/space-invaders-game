import pygame

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 600)) ## create a screen

# while True:
#     pass -> using this syntax will make the program run forever so system will hang

#to prevent the system from hanging, we can use events
# Events are actions that are detected by the program like closing the window,pressing mouse button, pressing keyboard key etc..

for event in pygame.event.get(): # get all the events that are happening
    print(event)

# <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 0})>
# <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 1})>
# <Event(32774-WindowShown {'window': None})>
# <Event(32768-ActiveEvent {'gain': 1, 'state': 2})>
# <Event(32785-WindowFocusGained {'window': None})>
# <Event(770-TextEditing {'text': '', 'start': 0, 'length': 0, 'window': None})>
# <Event(32768-ActiveEvent {'gain': 1, 'state': 1})>
# <Event(32783-WindowEnter {'window': None})>
# <Event(1024-MouseMotion {'pos': (579, 450), 'rel': (0, 0), 'buttons': (0, 0, 0), 'touch': False, 'window': None})>
# <Event(1024-MouseMotion {'pos': (579, 451), 'rel': (0, 1), 'buttons': (0, 0, 0), 'touch': False, 'window': None})>
# <Event(32770-VideoExpose {})>
# <Event(32776-WindowExposed {'window': None})>