import React from 'react';

const SeverityGauge = ({ score }) => {
  const normalizedScore = score ? Math.min(100, Math.max(0, score)) : 0;
  
  let color = 'var(--color-healthy)';
  let label = 'Low Risk';
  
  if (normalizedScore >= 20) {
    color = 'var(--color-mild)';
    label = 'Moderate Risk';
  }
  if (normalizedScore >= 60) {
    color = 'var(--color-severe)';
    label = 'High Risk';
  }

  return (
    <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.4s', textAlign: 'center' }}>
      <h3 style={{ marginBottom: '1rem', textAlign: 'left' }}>Severity Score</h3>
      
      <div style={{ position: 'relative', width: '150px', height: '150px', margin: '0 auto' }}>
        <svg viewBox="0 0 100 100" style={{ transform: 'rotate(-90deg)', width: '100%', height: '100%' }}>
          {/* Background circle */}
          <circle 
            cx="50" cy="50" r="40" 
            fill="none" 
            stroke="rgba(255,255,255,0.1)" 
            strokeWidth="10" 
          />
          {/* Progress circle */}
          <circle 
            cx="50" cy="50" r="40" 
            fill="none" 
            stroke={color} 
            strokeWidth="10" 
            strokeDasharray={`${(normalizedScore / 100) * 251.2} 251.2`}
            strokeLinecap="round"
            style={{ transition: 'stroke-dasharray 1s ease-out, stroke 0.5s ease' }}
          />
        </svg>
        
        <div style={{
          position: 'absolute',
          top: '0', left: '0', right: '0', bottom: '0',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          <span style={{ fontSize: '2rem', fontWeight: 'bold', color: '#fff' }}>
            {Math.round(normalizedScore)}
          </span>
        </div>
      </div>
      
      <div style={{ marginTop: '1rem', fontWeight: '500', color: color }}>
        {label}
      </div>
    </div>
  );
};

export default SeverityGauge;
