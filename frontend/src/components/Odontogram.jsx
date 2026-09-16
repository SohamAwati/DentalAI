import React from 'react';

const Odontogram = ({ imageSrc, teethData }) => {
  if (!imageSrc) {
    return (
      <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.3s', minHeight: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <p style={{ color: 'var(--text-secondary)' }}>Upload an image to see detection results</p>
      </div>
    );
  }

  const getColor = (condition) => {
    switch(condition) {
      case 'healthy': return 'var(--color-healthy)';
      case 'mild': return 'var(--color-mild)';
      case 'moderate': return 'var(--color-moderate)';
      case 'severe': return 'var(--color-severe)';
      default: return 'var(--accent-blue)';
    }
  };

  return (
    <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.3s' }}>
      <h3 style={{ marginBottom: '1rem' }}>Detection View</h3>
      
      <div style={{ position: 'relative', width: '100%', overflow: 'hidden', borderRadius: 'var(--radius-sm)' }}>
        <img 
          src={imageSrc} 
          alt="Dental Scan" 
          style={{ width: '100%', height: 'auto', display: 'block' }} 
        />
        
        {teethData && teethData.map((tooth, idx) => {
          const [x, y, w, h] = tooth.boundingBox;
          const color = getColor(tooth.condition);
          
          return (
            <div 
              key={idx}
              style={{
                position: 'absolute',
                left: `${x}%`,
                top: `${y}%`,
                width: `${w}%`,
                height: `${h}%`,
                border: `2px solid ${color}`,
                backgroundColor: 'rgba(0,0,0,0.1)',
                boxShadow: `0 0 10px ${color}55`,
                cursor: 'pointer',
                transition: 'all 0.2s ease',
              }}
              title={`Tooth ${tooth.tooth_number} - ${tooth.condition} (${Math.round(tooth.confidence * 100)}%)`}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = `${color}44`;
                e.currentTarget.style.transform = 'scale(1.05)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = 'rgba(0,0,0,0.1)';
                e.currentTarget.style.transform = 'scale(1)';
              }}
            >
              <div style={{
                position: 'absolute',
                top: '-20px',
                left: '0',
                background: color,
                color: '#fff',
                fontSize: '10px',
                padding: '2px 4px',
                borderRadius: '4px',
                fontWeight: 'bold',
                whiteSpace: 'nowrap'
              }}>
                {tooth.condition}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Odontogram;
