import React, { useState, useRef } from 'react';

const UploadPanel = ({ onUpload }) => {
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef(null);

  const handleDragEnter = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onUpload(e.dataTransfer.files[0]);
    }
  };

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      onUpload(e.target.files[0]);
    }
  };

  return (
    <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.1s' }}>
      <h2 className="gradient-text">Upload X-Ray Scan</h2>
      <p style={{ marginBottom: '1.5rem' }}>Drag and drop a dental scan here, or click to browse files.</p>
      
      <div 
        style={{
          border: `2px dashed ${isDragging ? 'var(--accent-teal)' : 'rgba(255,255,255,0.2)'}`,
          borderRadius: 'var(--radius-lg)',
          padding: '3rem 2rem',
          textAlign: 'center',
          cursor: 'pointer',
          background: isDragging ? 'rgba(0, 210, 255, 0.05)' : 'rgba(0,0,0,0.2)',
          transition: 'all 0.3s ease',
          boxShadow: isDragging ? '0 0 20px rgba(0, 210, 255, 0.2)' : 'none'
        }}
        onDragEnter={handleDragEnter}
        onDragLeave={handleDragLeave}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current.click()}
      >
        <div style={{ fontSize: '3rem', marginBottom: '1rem', color: 'var(--accent-teal)' }}>
          📸
        </div>
        <h3 style={{ margin: '0 0 0.5rem 0' }}>Select an Image</h3>
        <p style={{ fontSize: '0.9rem', margin: 0 }}>Supports JPG, PNG (Max 5MB)</p>
        
        <input 
          type="file" 
          ref={fileInputRef} 
          onChange={handleFileChange} 
          accept="image/*" 
          style={{ display: 'none' }} 
        />
      </div>
    </div>
  );
};

export default UploadPanel;
