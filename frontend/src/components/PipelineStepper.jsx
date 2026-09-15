import React from 'react';

const PipelineStepper = ({ status }) => {
  // status can be: idle, uploading, processing, done, error
  const steps = [
    { id: 'upload', label: 'Upload' },
    { id: 'quality', label: 'Quality Check' },
    { id: 'detect', label: 'AI Detection' },
    { id: 'analyze', label: 'Analysis' }
  ];
  
  let currentStepIdx = 0;
  if (status === 'uploading') currentStepIdx = 0;
  if (status === 'processing') currentStepIdx = 2; // jump to detection visually
  if (status === 'done') currentStepIdx = 4;
  if (status === 'error') currentStepIdx = -1;

  return (
    <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.2s', padding: '1.5rem' }}>
      <h3 style={{ marginBottom: '1rem', fontSize: '1.1rem' }}>Pipeline Status</h3>
      
      <div style={{ display: 'flex', justifyContent: 'space-between', position: 'relative' }}>
        {/* Progress Line */}
        <div style={{ 
          position: 'absolute', 
          top: '15px', 
          left: '10%', 
          right: '10%', 
          height: '2px', 
          background: 'rgba(255,255,255,0.1)', 
          zIndex: 0 
        }}>
          <div style={{
            height: '100%',
            background: 'linear-gradient(90deg, var(--accent-teal), var(--accent-blue))',
            width: `${Math.min(100, Math.max(0, (currentStepIdx / (steps.length - 1)) * 100))}%`,
            transition: 'width 0.5s ease'
          }}></div>
        </div>

        {steps.map((step, idx) => {
          const isCompleted = currentStepIdx > idx;
          const isActive = currentStepIdx === idx;
          const isError = status === 'error' && isActive;
          
          let bgColor = 'rgba(30, 30, 45, 1)';
          let borderColor = 'rgba(255,255,255,0.2)';
          let textColor = 'var(--text-secondary)';
          
          if (isCompleted) {
            bgColor = 'var(--accent-blue)';
            borderColor = 'var(--accent-blue)';
            textColor = '#fff';
          } else if (isActive) {
            bgColor = 'var(--bg-primary)';
            borderColor = 'var(--accent-teal)';
            textColor = 'var(--accent-teal)';
          }
          
          if (isError) {
            borderColor = 'var(--color-severe)';
            textColor = 'var(--color-severe)';
          }

          return (
            <div key={step.id} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', zIndex: 1, position: 'relative' }}>
              <div style={{
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: bgColor,
                border: `2px solid ${borderColor}`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '0.8rem',
                fontWeight: 'bold',
                color: isCompleted ? '#fff' : 'inherit',
                transition: 'all 0.3s ease',
                boxShadow: isActive && !isError ? '0 0 10px rgba(0, 210, 255, 0.5)' : 'none'
              }}>
                {isCompleted ? '✓' : (idx + 1)}
              </div>
              <div style={{ 
                marginTop: '0.5rem', 
                fontSize: '0.75rem', 
                color: textColor,
                fontWeight: isActive ? '600' : '400' 
              }}>
                {step.label}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PipelineStepper;
