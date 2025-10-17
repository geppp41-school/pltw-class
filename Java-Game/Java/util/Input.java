package util;

import static org.lwjgl.glfw.GLFW.glfwSetKeyCallback;

public class Input {

    

    public static void initialize(Long windowId){
        glfwSetKeyCallback(windowId, (window, key, scancode, action, mods) -> {
            System.out.println("\n");
            System.out.println("window: " + window);
            System.out.println("key: " + key);
            System.out.println("scancode: " + scancode);
            System.out.println("action: " + action);
            System.out.println("mods: " + mods);
        });
    }
}