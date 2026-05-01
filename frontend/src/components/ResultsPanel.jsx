import {
  RadialBarChart,
  RadialBar,
  PolarAngleAxis,
  ResponsiveContainer,
} from 'recharts';
import styles from './ResultsPanel.module.css';

function getRiskLevel(probability) {
  if (probability >= 0.7) return { label: 'High Risk', color: '#f87171', emoji: '🔴' };
  if (probability >= 0.3) return { label: 'Moderate Risk', color: '#fbbf24', emoji: '🟡' };
  return { label: 'Low Risk', color: '#34d399', emoji: '🟢' };
}

function RiskGauge({ probability }) {
  const pct = Math.round(probability * 100);
  const { label, color } = getRiskLevel(probability);

  const data = [{ value: pct, fill: color }];

  return (
    <div className={styles.gaugeWrapper}>
      <ResponsiveContainer width="100%" height={220}>
        <RadialBarChart
          cx="50%"
          cy="60%"
          innerRadius="60%"
          outerRadius="90%"
          startAngle={180}
          endAngle={0}
          data={data}
          barSize={18}
        >
          <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
          <RadialBar
            background={{ fill: 'rgba(255,255,255,0.05)' }}
            dataKey="value"
            cornerRadius={10}
          />
        </RadialBarChart>
      </ResponsiveContainer>
      <div className={styles.gaugeCenter}>
        <span className={styles.gaugePercent} style={{ color }}>
          {pct}%
        </span>
        <span className={styles.gaugeLabel} style={{ color }}>
          {label}
        </span>
      </div>
    </div>
  );
}

function InsightBadge({ name, impact }) {
  const isHigh = impact === 'high';
  return (
    <div className={`${styles.insightBadge} ${isHigh ? styles.insightHigh : styles.insightMod}`}>
      <span className={styles.insightDot} />
      {name}
    </div>
  );
}

export default function ResultsPanel({ result, loading, error }) {
  if (loading) {
    return (
      <div className="card">
        <div className={styles.placeholder}>
          <div className={styles.spinner} />
          <p>Analyzing patient data…</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <div className={styles.placeholder}>
          <span style={{ fontSize: '2.5rem' }}>⚠️</span>
          <p style={{ color: '#f87171' }}>{error}</p>
        </div>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="card">
        <div className={styles.readyState}>
          <h3>👈 Ready for Analysis</h3>
          <p>Fill in the patient data and click "Generate Diagnostic Report".</p>
          {result?.simulated && (
            <p className={styles.simNote}>
              ⚠️ Running in demo mode — backend not connected.
            </p>
          )}
        </div>
      </div>
    );
  }

  const { probability, topRiskFactors, simulated } = result;
  const { label, color, emoji } = getRiskLevel(probability);

  return (
    <div className="card">
      <div className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>🔍 Diagnostic Analysis</h2>
        <p className={styles.cardSub}>AI-powered cardiac risk assessment results</p>
        {simulated && (
          <span className={styles.demoBadge}>🔬 Demo Mode</span>
        )}
      </div>

      <div className={styles.divider} />

      <RiskGauge probability={probability} />

      <div className={styles.riskBadge} style={{ borderColor: color, color }}>
        {emoji} {label} — {Math.round(probability * 100)}% Cardiac Risk Probability
      </div>

      {topRiskFactors && topRiskFactors.length > 0 && (
        <div className={styles.insightsSection}>
          <h3 className={styles.insightsTitle}>📊 AI-Powered Insights</h3>
          <p className={styles.insightsSub}>Top contributing risk factors detected:</p>
          <div className={styles.insightsList}>
            {topRiskFactors.map((f) => (
              <InsightBadge key={f.name} name={f.name} impact={f.impact} />
            ))}
          </div>
        </div>
      )}

      <div className={styles.disclaimer}>
        ⚠️ This tool is for informational purposes only and is not a substitute for professional medical advice.
      </div>
    </div>
  );
}
