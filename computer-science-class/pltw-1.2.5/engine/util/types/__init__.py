
from tkinter import Canvas, Label, PhotoImage, Tk, ttk
from PIL import Image, ImageTk
import PIL.ImageFile as ImageFile

class Int(int):
    pass
class Float(float):
    pass
class List(list):
    pass
class Dictionary(dict):
    pass
class Transform:
    def __init__(self) -> None:
        self.Position:Vector2 = Vector2(0.0, 0.0)
        self.Rotation:float = 0.0
        self.Scale:Vector2 = Vector2(1.0, 1.0)
        self.Size:Vector2 = Vector2(1.0, 1.0)
        pass

class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

class Object:
    def __init__(self) -> None:
        self.transform:Transform = Transform()
        pass
    pass

class TexturedObject(Object):
    def __init__(self,screen_root:Tk , texture:ImageFile.ImageFile | PhotoImage | str) -> None:
        super().__init__()
        if(isinstance(texture, ImageFile.ImageFile)):
            self.texture = ImageTk.PhotoImage(texture)
        elif(isinstance(texture, PhotoImage)):
            self.texture = texture
        elif(isinstance(texture, str)):
            image = Image.open(texture)
            self.texture = ImageTk.PhotoImage(image)
        else:
            raise TypeError("Texture must be a File Path, PIL Image, or Tkinter PhotoImage")
        self.__objectLabel = ttk.Label(screen_root, image=self.texture)

    def place(self):
        self.__objectLabel.place(x=self.transform.Position.x, y=self.transform.Position.y)
    pass