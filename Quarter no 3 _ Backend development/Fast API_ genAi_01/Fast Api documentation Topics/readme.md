#### Create a Folder:

- First, create a folder where you'll organize your FastAPI project files. You can do this using your operating system's file manager or command-line interface.

## Run Uvicorn:

- Once you've created the folder and added your FastAPI application code (typically in a file named main.py), you can run the FastAPI application using the Uvicorn server.

Open a terminal or command prompt and navigate to the folder where your FastAPI application code is located.
Run the following command to start the FastAPI application:

## uvicorn main:app

- This command tells uvicorn to run your FastAPI application (main module, app instance). By default, uvicorn starts the server on port 8000.
Enable Auto-Reloading (Optional):

- If you want uvicorn to automatically reload your FastAPI application whenever changes are made to the code, you can use the --reload option.
Run the following command to start the FastAPI application with auto-reloading enabled:

## uvicorn main:app --reload

With auto-reloading enabled, uvicorn will monitor your project files for changes, and whenever you save changes to a file, uvicorn will automatically restart the server to apply those changes.


## API Testing Tools:

1. Thunder Client: This is an extension for Visual Studio Code (VSCode) that allows you to test APIs directly within the editor.
2. Postman: Postman is a popular API development tool that allows you to design, test, and debug APIs. It provides a user-friendly interface for making HTTP requests and inspecting responses.

3. HTTPie: HTTPie is a command-line HTTP client that makes it easy to interact with APIs. It provides a simple syntax for sending HTTP requests and displaying responses.

## Installing Dependencies:

1. pip install requests: This installs the requests library, which is commonly used for making HTTP requests in Python.
2. pip install fastapi: This installs the FastAPI framework, which is a modern, fast web framework for building APIs with Python.
3. pip install uvicorn: This installs Uvicorn, which is a lightning-fast ASGI server for running Python web applications.

### Request body:
- When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
- To declare a request body, you use Pydantic models with all their power and  benefits                                    
## pip install pydantic