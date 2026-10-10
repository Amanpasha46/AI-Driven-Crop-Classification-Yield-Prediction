# AI-Driven-Crop-Classification-Yield-Prediction
For your AI Driven Crop Classification & Yield Prediction project, install these requirements.

1. Backend — Python

From PowerShell:

cd "C:\Users\aiman\Desktop\new\AI_Crop_Prediction"

.\venv\Scripts\Activate.ps1

If the virtual environment does not exist:

python -m venv venv
.\venv\Scripts\Activate.ps1

Then install:

pip install fastapi uvicorn requests pandas numpy scikit-learn joblib sqlalchemy python-multipart

2. Backend requirements.txt

Create/update:

fastapi
uvicorn
requests
pandas
numpy
scikit-learn
joblib
sqlalchemy
python-multipart

Then you can install everything with:

pip install -r requirements.txt

3. Frontend — Node.js

Check Node and npm:

node --version
npm --version

You need Node.js installed. Then:

cd "C:\Users\aiman\Desktop\new\AI_Crop_Prediction\frontend"

Install the frontend packages:

npm install

Your package.json should include at least:

{
  "name": "ai-crop-prediction-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.7.9",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^7.1.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.4",
    "vite": "^6.0.7"
  }
}

Then:

npm install

4. Complete installation commands

You can run these in order:

cd "C:\Users\aiman\Desktop\new\AI_Crop_Prediction"

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

cd frontend

npm install

5. Start the backend

From the project root:

cd "C:\Users\aiman\Desktop\new\AI_Crop_Prediction"

.\venv\Scripts\Activate.ps1

uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

Backend:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs

6. Start the frontend

Open a second PowerShell window:

cd "C:\Users\aiman\Desktop\new\AI_Crop_Prediction\frontend"

npm run dev

Frontend:

http://localhost:5173

Important

You do not need to install these separately:

pandas already handles CSV processing

scikit-learn handles the Random Forest models

joblib loads your .joblib models

SQLAlchemy handles the database

requests calls Open-Meteo/location APIs

axios handles frontend API calls

react-router-dom handles frontend pages

lucide-react is not required for the current frontend


Also, do not install torch, TensorFlow, Ollama, or CUDA for the current version of this project.


## Local setup (Windows)

The backend defaults to a local SQLite database, so PostgreSQL is not required for a basic local run.

1. Open a terminal in this project folder.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install backend dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Start the API from the project root:
   ```powershell
   python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```
5. Open the API docs at http://127.0.0.1:8000/docs.
6. In a second terminal, install and start the frontend:
   ```powershell
   cd frontend
   npm install
   npm run dev
   ```
7. Open the Vite URL shown in the terminal (normally http://localhost:5173).

The API may need internet access for live location, weather, and climate data. The first backend startup creates a local `crop_prediction.db` file automatically. Do not commit `.env` files or database files containing personal data.
