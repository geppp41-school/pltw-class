
from tkinter import RIGHT, Canvas, Label, PhotoImage, Tk, ttk
from PIL import Image, ImageTk
import PIL.ImageFile as ImageFile
import math

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

    def rotated(self, angle_degrees: float):
        x = self.x
        y = self.y
        self.x = x*math.cos(math.radians(angle_degrees)) - y*math.sin(math.radians(angle_degrees))
        self.y = x*math.sin(math.radians(angle_degrees)) + y*math.cos(math.radians(angle_degrees))

    def RIGHT(self):
        return Vector2(1.0, 0.0)
    def LEFT(self):
        return Vector2(-1.0, 0.0)
    def UP(self):
        return Vector2(0.0, 1.0)
    def DOWN(self):
        return Vector2(0.0, -1.0)

class Object:
    def __init__(self) -> None:
        self.transform:Transform = Transform()
        pass
    pass

class TexturedObject(Object):
    def __init__(self,screen_root:Tk , texture:ImageFile.ImageFile | str) -> None:
        super().__init__()
        if(isinstance(texture, ImageFile.ImageFile)):
            self.textureImage = texture
            self.photoImageTexture = ImageTk.PhotoImage(texture)
            self.texture = self.photoImageTexture
        elif(isinstance(texture, str)):
            self.textureImage = Image.open(texture)
            self.photoImageTexture = ImageTk.PhotoImage(self.textureImage)
            self.texture = self.photoImageTexture
            
        else:
            raise TypeError(f"Texture must be a File Path or PIL Image\n Got: {type(texture)}")
        self.__objectLabel = ttk.Label(screen_root, image=self.texture)

    def place(self):
        rotatedTexture = self.textureImage.rotate(self.transform.Rotation%360)
        self.photoImageTexture = ImageTk.PhotoImage(rotatedTexture)
        self.__objectLabel.configure(image=self.photoImageTexture)
        self.__objectLabel.place(x=self.transform.Position.x, y=self.transform.Position.y)
    pass