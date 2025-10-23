

A web-based tool to automate code reviews by analyzing source code for readability, modularity, and potential bugs using a local LLM (microsoft/phi-2). The project features a React frontend for file uploads and result display, and a FastAPI backend integrated with the LLM for code analysis.

Features





File Upload: Upload code files (e.g., .py) via a user-friendly React interface.



Automated Code Review: Leverages microsoft/phi-2 LLM to provide suggestions on code readability, modularity, and potential bugs.



Responsive UI: Clean, modern frontend design with plain CSS for a professional look.



API-Driven: FastAPI backend handles file processing and LLM integration.



Extensible: Modular structure for easy additions (e.g., database for storing reviews).

Project Structure

Code-Review-Assistant/
├── code-review-frontend/      # React frontend
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── App.css           # Custom CSS styling
│   │   ├── index.js          # React entry point
│   │   └── ...
│   ├── public/
│   │   ├── index.html        # HTML template
│   │   └── ...
│   ├── package.json          # Node.js dependencies
│   └── ...
├── code-review-backend/       # FastAPI backend
│   ├── main.py               # FastAPI server
│   ├── llm_client.py         # LLM integration
│   ├── requirements.txt       # Python dependencies
│   └── ...
├── demo.mp4                  # Demo video (optional, or linked externally)
├── README.md                 # This file
└── .gitignore                # Git ignore rules

Prerequisites





Python 3.8+: For running the FastAPI backend and LLM.



Node.js 14+: For running the React frontend.



Git: For cloning and managing the repository.



Hardware: A GPU is recommended for faster LLM processing (CPU works but is slower).

Setup Instructions

Backend Setup





Navigate to the backend directory:

cd code-review-backend



Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install dependencies:

pip install -r requirements.txt



Run the FastAPI server:

uvicorn main:app --reload

The backend will be available at http://localhost:8000.

Frontend Setup





Navigate to the frontend directory:

cd code-review-frontend



Install dependencies:

npm install



Start the React app:

npm start

The frontend will be available at http://localhost:3000.

Usage





Ensure the backend is running (http://localhost:8000).



Open the frontend in a browser (http://localhost:3000).



Upload a code file (e.g., .py) using the file input.



Click "Submit for Review" to receive LLM-generated suggestions.



View the review output displayed below, including suggestions for readability, modularity, and potential bugs.

Example Input

Upload a file like sample.py:

def add_numbers(a, b):
    result = a + b
    return result

def main():
    x = 10
    y = 20
    print(add_numbers(x, y))
    print(add_numbers(x, "five"))

main()

The tool will analyze it for input type handling, modularity, and suggest improvements like adding type checks.

 Example Output:

 - The code is well-structured and easy to read.
- The function can be further improved by adding type hints.
- The code could be further improved by adding more modular functions.
- The code could be improved by using a try-except block to handle the error in the add_numbers function.

Solution:

```python
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers"""
    result = a + b
    print("Sum is", result)
    return result

def main():
    x = 10
    y = 20
    add_numbers(x, y)
    add_numbers(x, "five")

main()
```
