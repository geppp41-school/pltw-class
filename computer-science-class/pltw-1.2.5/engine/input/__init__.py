from engine.screen import _root

_keysPressed = []

#_root.bind("<KeyPress>", lambda event: _keysPressed.append(event.keysym))
#_root.bind("<KeyRelease>", lambda event: _keysPressed.remove(event.keysym))

def test(key):
    print(key)

_root.bind("<KeyPress>", test)