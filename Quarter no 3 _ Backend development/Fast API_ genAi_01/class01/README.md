Install poetry: https://www.youtube.com/watch?v=5lioBm8f324

 In windows powershell >>> run as Administrator 
 
Step1: install poetry from this link 
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py –

Step2: set environment variable
•	In the System Properties window, click on the "Environment Variables" button.
•	In the Environment Variables window, under "System variables", find the "Path" variable and select it, then click "Edit".
•	Add the path to the directory where Poetry is installed at the end of the existing list.
•	C:\Users\Arooj\AppData\Roaming\pypoetry\venv\Scripts
•	Click "OK" to close all windows.

After adding this path to the PATH variable, PowerShell should recognize Poetry commands without specifying the full path to the script’s directory.
Once you've done this, close and reopen your PowerShell session and try running poetry --version again. It should now recognize the command and display the version information.



