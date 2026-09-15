import React from 'react';

const InsightsPanel = ({ insights }) => {
  if (!insights) {
    return (
      <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.5s', gridColumn: '1 / -1' }}>
        <h3 style={{ marginBottom: '1rem' }}>Personalized Insights</h3>
        <p>Insights will appear here after analysis.</p>
      </div>
    );
  }

  return (
    <div className="glass-panel animate-slide-up" style={{ animationDelay: '0.5s', gridColumn: '1 / -1' }}>
      <h3 style={{ marginBottom: '1.5rem' }}>Personalized Insights & Patterns</h3>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        
        {/* Archetype / Clusters */}
        <div style={{ background: 'rgba(0,0,0,0.2)', padding: '1.5rem', borderRadius: 'var(--radius-md)' }}>
          <h4 style={{ color: 'var(--accent-teal)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>👥</span> Cohort Analysis
          </h4>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            {insights.clusters && insights.clusters.map((cluster, idx) => (
              <li key={idx} style={{ 
                marginBottom: '0.75rem', 
                padding: '0.75rem', 
                background: 'rgba(255,255,255,0.05)', 
                borderRadius: 'var(--radius-sm)',
                borderLeft: '3px solid var(--accent-blue)'
              }}>
                {cluster}
              </li>
            ))}
          </ul>
        </div>

        {/* Association Rules */}
        <div style={{ background: 'rgba(0,0,0,0.2)', padding: '1.5rem', borderRadius: 'var(--radius-md)' }}>
          <h4 style={{ color: 'var(--accent-purple)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>🔍</span> Predictive Rules Found
          </h4>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {insights.association_rules && insights.association_rules.map((ruleObj, idx) => (
              <div key={idx} style={{ 
                padding: '0.75rem', 
                background: 'rgba(255,255,255,0.05)', 
                borderRadius: 'var(--radius-sm)',
                display: 'flex',
                flexDirection: 'column',
                gap: '0.25rem'
              }}>
                <div style={{ fontWeight: '500' }}>{ruleObj.rule}</div>
                <div style={{ display: 'flex', gap: '1rem', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                  <span>Support: {(ruleObj.support * 100).toFixed(0)}%</span>
                  <span>Confidence: {(ruleObj.confidence * 100).toFixed(0)}%</span>
                </div>
              </div>
            ))}
          </div>
        </div>
        
      </div>
    </div>
  );
};

export default InsightsPanel;
