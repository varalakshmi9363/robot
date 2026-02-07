import PyInstaller.__main__
import shutil
import os

def build():
    print("Building AI Robot CLI...")
    
    # ensure dist exists
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    
    PyInstaller.__main__.run([
        'src/main.py',
        '--onefile',
        '--name=ai-robot',
        '--clean',
        '--add-data=src/prompt.py;src', # Example of adding data if needed, though prompt is code here.
    ])
    
    print("Build complete. Executable is in dist/ai-robot.exe")

if __name__ == "__main__":
    build()
