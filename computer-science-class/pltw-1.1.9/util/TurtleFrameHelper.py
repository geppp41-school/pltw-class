from PIL import Image

def extract_fames(path, frameCount, outputPath):
    with Image.open(path) as immage:
        try:
            for i in range(frameCount):
                immage.seek(i)
                immage.save(outputPath+str(i)+".gif")

        except EOFError:
            print("Frame does not exist")