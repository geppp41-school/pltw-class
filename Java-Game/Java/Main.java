import static org.lwjgl.system.MemoryUtil.NULL;

import util.Window;

public class Main {
    private static Window mainWindow;
    public static void main(String[] args) {
        mainWindow = new Window(700, 300, "null", NULL, NULL);
        mainWindow.mainLoop();
        System.out.println("Closed Window");
    }
}