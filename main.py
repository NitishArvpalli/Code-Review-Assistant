from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from llm_client import LocalLLM

app = FastAPI(title="Simple Code Review Assistant")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Initialize the local LLM once on startup
llm = LocalLLM(model_name="microsoft/phi-2")

@app.post("/review")
async def review_code(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        code_text = contents.decode("utf-8")

        if not code_text.strip():
            raise HTTPException(status_code=400, detail="Empty code file")

        suggestions = llm.generate_review(code_text)

        return {
            "filename": file.filename,
            "review_summary": suggestions
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
