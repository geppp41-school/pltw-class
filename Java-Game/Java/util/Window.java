package util;
import static org.lwjgl.glfw.GLFW.GLFW_FALSE;
import static org.lwjgl.glfw.GLFW.GLFW_KEY_ESCAPE;
import static org.lwjgl.glfw.GLFW.GLFW_RELEASE;
import static org.lwjgl.glfw.GLFW.GLFW_RESIZABLE;
import static org.lwjgl.glfw.GLFW.GLFW_TRUE;
import static org.lwjgl.glfw.GLFW.GLFW_VISIBLE;
import static org.lwjgl.glfw.GLFW.glfwCreateWindow;
import static org.lwjgl.glfw.GLFW.glfwDefaultWindowHints;
import static org.lwjgl.glfw.GLFW.glfwInit;
import static org.lwjgl.glfw.GLFW.glfwMakeContextCurrent;
import static org.lwjgl.glfw.GLFW.glfwPollEvents;
import static org.lwjgl.glfw.GLFW.glfwSetErrorCallback;
import static org.lwjgl.glfw.GLFW.glfwSetKeyCallback;
import static org.lwjgl.glfw.GLFW.glfwSetWindowShouldClose;
import static org.lwjgl.glfw.GLFW.glfwShowWindow;
import static org.lwjgl.glfw.GLFW.glfwSwapBuffers;
import static org.lwjgl.glfw.GLFW.glfwSwapInterval;
import static org.lwjgl.glfw.GLFW.glfwWindowHint;
import static org.lwjgl.glfw.GLFW.glfwWindowShouldClose;
import static org.lwjgl.opengl.GL11.GL_COLOR_BUFFER_BIT;
import static org.lwjgl.opengl.GL11.GL_DEPTH_BUFFER_BIT;
import static org.lwjgl.opengl.GL11.glClear;
import static org.lwjgl.system.MemoryUtil.NULL;

import org.joml.Vector2i;
import org.lwjgl.glfw.GLFWErrorCallback;
import org.lwjgl.opengl.GL;

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
        
        glfwSetKeyCallback(this.id, (window, key, scancode, action, mods) -> {
			if ( key == GLFW_KEY_ESCAPE && action == GLFW_RELEASE )
				glfwSetWindowShouldClose(window, true); // We will detect this in the rendering loop
		});
        
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

    public Long getId(){
        return this.id;
    }
}
