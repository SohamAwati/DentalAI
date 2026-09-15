# DentalAI Diagnostics 🦷

DentalAI is an end-to-end, AI-powered dental caries detection and risk assessment application. It utilizes a fine-tuned YOLOv8 classification model trained on the Mendeley Caries-Spectra dataset to identify enamel caries from dental X-ray images, providing real-time severity scoring and patient archetypes through a premium, glassmorphic React interface.

## Features ✨
- **Real-time AI Inference:** Uses a YOLOv8 Image Classification model fine-tuned on clinical dataset (Caries-Spectra).
- **FastAPI Backend:** A fast, asynchronous Python backend handling image processing and inference.
- **Modern React Frontend:** Built with Vite and React, featuring a sleek dark-mode glassmorphic design system.
- **Interactive Odontogram:** Upload scans and instantly see visual feedback and risk stratification (Healthy, Mild, Severe).
- **Predictive Insights:** Calculates an overall risk score and maps patients to clinical archetypes based on AI predictions.

## Project Structure 📁
```
DentalAI/
├── backend/               # FastAPI backend and ML pipeline
│   ├── app/               # API routes and services
│   │   ├── main.py        # Entry point for FastAPI
│   │   └── services/      # Pipeline logic and YOLOv8 inference wrapper
│   ├── ml/                # Machine learning training scripts
│   └── runs_cls/          # Trained YOLOv8 model weights (best.pt)
└── frontend/              # React + Vite frontend
    ├── src/
    │   ├── components/    # Reusable UI components (UploadPanel, SeverityGauge, etc.)
    │   ├── api.js         # Axios integration with backend
    │   └── App.jsx        # Main application state and orchestration
```

## Getting Started 🚀

### Prerequisites
- Node.js (v18+)
- Python (3.10+)
- `npm` or `yarn`

### 1. Start the Backend (FastAPI)
Navigate to the backend directory, install dependencies, and start the development server:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
The backend will run on `http://127.0.0.1:8000`. API documentation is available at `http://127.0.0.1:8000/docs`.

### 2. Start the Frontend (React + Vite)
Open a new terminal window, navigate to the frontend directory, install dependencies, and start the development server:
```bash
cd frontend
npm install
npm run dev
```
The frontend will run on `http://localhost:5173`. Open this URL in your browser to interact with DentalAI.

## Usage 💡
1. Navigate to the frontend web app.
2. Drag and drop a dental X-ray image into the **Upload X-Ray Scan** zone.
3. Watch the pipeline stepper progress as the image is processed by the AI backend.
4. Review the AI prediction, severity score, and patient archetype insights.

## Model Details 🧠
The AI model powering this application is a **YOLOv8-nano classification model** (`yolov8n-cls.pt`). It was retrained using the **Caries-Spectra dataset**, classifying images into three distinct categories:
- `NoEnamel_Caries` $\rightarrow$ Healthy
- `EarlyStageEnamel_Caries` $\rightarrow$ Mild Risk
- `AdvanceEnamel_Caries` $\rightarrow$ Severe / High Risk

## License 📄
This project is licensed under the MIT License.
