import org.lwjgl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.opengl.*;
import org.lwjgl.system.*;

import java.nio.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;
import static org.lwjgl.system.MemoryStack.*;
import static org.lwjgl.system.MemoryUtil.*;

public class Window {

    private Long window;

    public Window(int width, int height, String name, long monitor, long share)
    {
        this.window = glfwCreateWindow(width, height, name, monitor, share);
    }
    public Window(int width, int height, String name)
    {
        this.window = glfwCreateWindow(width, height, name, NULL, NULL);
    }
}
