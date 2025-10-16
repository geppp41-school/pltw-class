import org.joml.Vector2i;
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

public class Window{

    private Long id;
    private GLFWErrorCallback errorCallback;
    private Vector2i screenSize;
    private Boolean resizable = false;

    public Window(int width, int height, String name, long monitor, long share)
    {

        glfwSetErrorCallback(this.errorCallback=GLFWErrorCallback.createPrint(System.err));
        if( glfwInit() != true ){
            throw new IllegalStateException("Unable to initialize GLFW");
        } else {
            System.out.println("\u001B[32mInitialized GLFW\u001B[0m");
        }
        //loading window settings
        glfwDefaultWindowHints();
        glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);
        glfwWindowHint(GLFW_RESIZABLE, resizable ? GLFW_TRUE : GLFW_FALSE);
        

        this.screenSize = new Vector2i(width,height);
        this.id = glfwCreateWindow(width, height, name, monitor, share);
        //check if window is created
        if(this.id == NULL){
             throw new RuntimeException("Failed to create window");
        } else {
            System.out.println("\u001B[32mCreated Window: \u001B[0m" + this.id);
        }

        glfwMakeContextCurrent(this.id);
        GL.createCapabilities();

        glfwSwapInterval(1); // How many draws to swap the buffer
        glfwShowWindow(this.id); // Shows the window
        
        
    }

    public void mainLoop(){
        while ( !glfwWindowShouldClose(this.id) ) {
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // clear the framebuffer

			glfwSwapBuffers(this.id); // swap the color buffers

			// Poll for window events. The key callback above will only be
			// invoked during this call.
			glfwPollEvents();
		}
    }
}
