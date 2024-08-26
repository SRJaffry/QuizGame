# QuizGame


# Creating and Running an Executable of Python Code

To create and run an executable of Python code, you'll typically follow these steps:

1. **Write Your Python Script**: Create a Python file (e.g., `script.py`) with the code you want to run.

2. **Convert the Python Script to an Executable**: Use a tool like `PyInstaller` or `cx_Freeze` to package your Python script into an executable file (.exe on Windows, for example). 

3. **Run the Executable**: Once the executable is created, you can run it like any other application.

## Step-by-Step Instructions Using PyInstaller

1. **Install PyInstaller**:

   Open your command prompt or terminal and run:

   ```bash
   pip install pyinstaller


2. **Create the Executables**:
   
   Navigate to the directory containing your Python script (script.py). Then, run:

   pyinstaller --onefile script.py

   * The --onefile option tells PyInstaller to bundle everything into a single executable file.

3. Locate the Executable:

   After PyInstaller finishes, it will create a dist directory in the same folder as your script. Inside dist, you will find the executable file (script.exe on Windows).

4. Run the Executable:

   Double-click the executable file or run it from the command line:
   
   ./dist/script



