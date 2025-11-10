import os
import subprocess

from sympy import true


try:
    cFiles = subprocess.getoutput("find ./computer-science-class/pltw-1.2.5 -name \"*.c\"").split("\n")
    for i in range(len(cFiles)):
        print(f"\033[33mcompiling \033[0m{cFiles[i]}")
        subprocess.call(f"gcc -shared -o {cFiles[i].replace(".c", ".so")} {cFiles[i]}", shell=True)
        print("\033[32mDone\033[0m")
    
    #resualt = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code {e.returncode}")
    print(f"Error output: {e.stderr}")
except FileNotFoundError:
    print("Command not found. Check if it's in your PATH.")