#  Code Review Assistant - Submission  

This project is a **Code Review Assistant** developed as part of the **Unthinkable Company Assignment**.  
It allows users to upload source code files and automatically generates a review report analyzing **readability**, **modularity**, and **potential bugs** using a **local LLM (Phi-2)** model.

---

##  Author Details  
**Name:** Nitish Arvapalli  
**Registration Number:** 22BCE3143  
**College:** Vellore Institute of Technology (VIT), Vellore  

---

##  Features  
- Upload source code file via frontend  
- Backend API processes the file and generates a review summary  
- Analyzes code for:
  - Readability  
  - Modularity  
  - Potential bugs  
- Returns concise improvement suggestions  
- Simple and interactive React-based UI  

---

##  Tech Stack  
- **Frontend:** React.js  
- **Backend:** FastAPI (Python)  
- **Model:** Microsoft Phi-2 (Local LLM)  
- **Middleware:** CORS for API communication  

---

## ⚙️ Setup Instructions  
### Backend  
```bash
pip install -r requirements.txt
uvicorn main:app --reload
### Frontend
cd frontend
npm install
npm start

