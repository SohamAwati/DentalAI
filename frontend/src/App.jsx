import React, { useState, useEffect } from 'react';
import './index.css';
import { scanImage, fetchInsights } from './api';

import UploadPanel from './components/UploadPanel';
import PipelineStepper from './components/PipelineStepper';
import Odontogram from './components/Odontogram';
import SeverityGauge from './components/SeverityGauge';
import InsightsPanel from './components/InsightsPanel';

function App() {
  const [pipelineStatus, setPipelineStatus] = useState('idle'); // idle, uploading, processing, done, error
  const [imagePreviewUrl, setImagePreviewUrl] = useState(null);
  const [scanResult, setScanResult] = useState(null);
  const [insightsData, setInsightsData] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  // Load insights on initial mount (as instructed in guide)
  useEffect(() => {
    loadInsights();
  }, []);

  const loadInsights = async () => {
    try {
      const data = await fetchInsights();
      setInsightsData(data);
    } catch (err) {
      console.error("Failed to load insights", err);
    }
  };

  const handleUpload = async (file) => {
    // Reset state
    setErrorMsg(null);
    setScanResult(null);
    
    // Create local preview
    const previewUrl = URL.createObjectURL(file);
    setImagePreviewUrl(previewUrl);
    
    try {
      setPipelineStatus('uploading');
      
      // Simulate slight delay for UI so user sees the step
      await new Promise(r => setTimeout(r, 600)); 
      
      setPipelineStatus('processing');
      const result = await scanImage(file);
      
      if (!result.quality_passed) {
        throw new Error(`Quality Check Failed: ${result.quality_reason}`);
      }
      
      setScanResult(result);
      setPipelineStatus('done');
      
    } catch (err) {
      setPipelineStatus('error');
      setErrorMsg(err.message || 'An error occurred during analysis.');
    }
  };

  return (
    <div className="app-container">
      <header style={{ marginBottom: '1rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2.5rem', margin: 0 }}>
          <span className="gradient-text">DentalAI</span> Diagnostics
        </h1>
        <p>AI-Powered Caries Detection & Risk Assessment</p>
      </header>

      <div className="dashboard-grid">
        {/* Main Column */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
          
          <PipelineStepper status={pipelineStatus} />
          
          {pipelineStatus === 'idle' || pipelineStatus === 'uploading' ? (
            <UploadPanel onUpload={handleUpload} />
          ) : (
            <Odontogram 
              imageSrc={imagePreviewUrl} 
              teethData={scanResult?.teeth} 
            />
          )}

          {errorMsg && (
            <div className="glass-panel animate-slide-up" style={{ borderLeft: '4px solid var(--color-severe)', backgroundColor: 'rgba(239, 68, 68, 0.1)' }}>
              <h3 style={{ color: 'var(--color-severe)' }}>Analysis Failed</h3>
              <p>{errorMsg}</p>
              <button 
                className="btn-primary" 
                style={{ marginTop: '1rem' }}
                onClick={() => setPipelineStatus('idle')}
              >
                Try Another Image
              </button>
            </div>
          )}

        </div>

        {/* Sidebar Column */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
          
          <SeverityGauge 
            score={scanResult?.overall_risk_score} 
          />
          
          {scanResult && scanResult.archetype && (
            <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.5s' }}>
              <h3 style={{ marginBottom: '0.5rem' }}>Patient Archetype</h3>
              <div style={{ 
                padding: '1rem', 
                background: 'rgba(0, 210, 255, 0.1)', 
                borderRadius: 'var(--radius-sm)',
                border: '1px solid var(--accent-teal)',
                color: 'var(--accent-teal)',
                fontWeight: '600',
                textTransform: 'capitalize'
              }}>
                {scanResult.archetype.replace(/-/g, ' ')}
              </div>
            </div>
          )}
          
        </div>
        
        {/* Full width bottom panel */}
        <InsightsPanel insights={insightsData} />
        
      </div>
    </div>
  );
}

export default App;
