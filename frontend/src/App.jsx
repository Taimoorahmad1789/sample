import { useState } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import InputForm from './components/InputForm';
import ResultsPanel from './components/ResultsPanel';
import styles from './App.module.css';

const DEFAULT_INPUTS = {
  age: 45,
  gender: 'Male',
  chestPain: 'Asymptomatic',
  restingBP: 120,
  cholesterol: 200,
  fastingBS: 'False',
  restECG: 'Normal',
  maxHR: 150,
  exerciseAngina: 'No',
  stDepression: 0.0,
  stSlope: 'Flat',
};

export default function App() {
  const [inputs, setInputs] = useState(DEFAULT_INPUTS);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (field, value) => {
    setInputs((prev) => ({ ...prev, [field]: value }));
  };

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(inputs),
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      // Simulate a result for demo purposes when the backend is not connected.
      const simulated = simulateResult(inputs);
      setResult(simulated);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.layout}>
      <Sidebar />
      <div className={styles.main}>
        <Header />
        <div className={styles.content}>
          <div className={styles.inputCol}>
            <InputForm
              inputs={inputs}
              onChange={handleChange}
              onAnalyze={handleAnalyze}
              loading={loading}
            />
          </div>
          <div className={styles.resultsCol}>
            <ResultsPanel result={result} loading={loading} error={error} />
          </div>
        </div>
      </div>
    </div>
  );
}

function simulateResult(inputs) {
  const riskFactors = [
    inputs.age > 60 ? 0.15 : inputs.age > 45 ? 0.08 : 0.02,
    inputs.gender === 'Male' ? 0.05 : 0.0,
    inputs.chestPain === 'Asymptomatic' ? 0.2 : inputs.chestPain === 'Typical Angina' ? 0.15 : 0.05,
    inputs.restingBP > 160 ? 0.15 : inputs.restingBP > 140 ? 0.08 : 0.0,
    inputs.cholesterol > 300 ? 0.12 : inputs.cholesterol > 240 ? 0.06 : 0.0,
    inputs.fastingBS === 'True' ? 0.08 : 0.0,
    inputs.exerciseAngina === 'Yes' ? 0.12 : 0.0,
    inputs.stDepression > 2 ? 0.1 : inputs.stDepression > 1 ? 0.05 : 0.0,
    inputs.maxHR < 120 ? 0.08 : inputs.maxHR < 150 ? 0.03 : 0.0,
  ];

  let probability = riskFactors.reduce((a, b) => a + b, 0);
  probability = Math.min(Math.max(probability + 0.05, 0.01), 0.99);

  // Build top risk factors from inputs that actually exceed clinical thresholds.
  const candidateFactors = [
    { name: 'Chest Pain Type', score: ['Asymptomatic', 'Typical Angina'].includes(inputs.chestPain) ? 0.2 : 0, impact: 'high' },
    { name: 'Age', score: inputs.age > 60 ? 0.15 : inputs.age > 45 ? 0.08 : 0, impact: inputs.age > 60 ? 'high' : 'moderate' },
    { name: 'Exercise-Induced Angina', score: inputs.exerciseAngina === 'Yes' ? 0.12 : 0, impact: 'high' },
    { name: 'Resting Blood Pressure', score: inputs.restingBP > 160 ? 0.15 : inputs.restingBP > 140 ? 0.08 : 0, impact: inputs.restingBP > 160 ? 'high' : 'moderate' },
    { name: 'Cholesterol', score: inputs.cholesterol > 300 ? 0.12 : inputs.cholesterol > 240 ? 0.06 : 0, impact: inputs.cholesterol > 300 ? 'high' : 'moderate' },
    { name: 'Fasting Blood Sugar', score: inputs.fastingBS === 'True' ? 0.08 : 0, impact: 'moderate' },
    { name: 'ST Depression', score: inputs.stDepression > 2 ? 0.1 : inputs.stDepression > 1 ? 0.05 : 0, impact: inputs.stDepression > 2 ? 'high' : 'moderate' },
    { name: 'Max Heart Rate', score: inputs.maxHR < 120 ? 0.08 : inputs.maxHR < 150 ? 0.03 : 0, impact: 'moderate' },
  ];
  const topRiskFactors = candidateFactors
    .filter((f) => f.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 3)
    .map(({ name, impact }) => ({ name, impact }));

  return { probability, topRiskFactors, simulated: true };
}
