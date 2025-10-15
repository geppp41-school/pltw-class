from Screen import Window

window = Window.Window()
window.bindKey("<Escape>", window.quit)#dont use () or it will call the function even if the key is not pressed
window.setBackgroundColor((0,0,0))
window.mainLoop()