import styles from './InputForm.module.css';

const GENDER_OPTIONS = ['Male', 'Female'];
const CHEST_PAIN_OPTIONS = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'];
const FBS_OPTIONS = ['False', 'True'];
const ECG_OPTIONS = ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'];
const ANGINA_OPTIONS = ['No', 'Yes'];
const SLOPE_OPTIONS = ['Upsloping', 'Flat', 'Downsloping'];

function Field({ label, children }) {
  return (
    <div className={styles.field}>
      <label className={styles.label}>{label}</label>
      {children}
    </div>
  );
}

function NumberInput({ value, onChange, min, max, step = 1 }) {
  return (
    <input
      type="number"
      className={styles.input}
      value={value}
      min={min}
      max={max}
      step={step}
      onChange={(e) => onChange(Number(e.target.value))}
    />
  );
}

function RangeInput({ value, onChange, min, max, step = 1 }) {
  return (
    <div className={styles.rangeWrapper}>
      <input
        type="range"
        className={styles.range}
        value={value}
        min={min}
        max={max}
        step={step}
        onChange={(e) => onChange(Number(e.target.value))}
      />
      <span className={styles.rangeValue}>{value}</span>
    </div>
  );
}

function Select({ value, onChange, options }) {
  return (
    <select
      className={styles.select}
      value={value}
      onChange={(e) => onChange(e.target.value)}
    >
      {options.map((opt) => (
        <option key={opt} value={opt}>
          {opt}
        </option>
      ))}
    </select>
  );
}

export default function InputForm({ inputs, onChange, onAnalyze, loading }) {
  return (
    <div className="card">
      <div className={styles.cardHeader}>
        <h2 className={styles.cardTitle}>📋 Patient Clinical Data</h2>
        <p className={styles.cardSub}>Enter accurate patient details for best prediction accuracy</p>
      </div>

      <div className={styles.divider} />

      <div className={styles.grid}>
        <Field label="👤 Age (years)">
          <NumberInput value={inputs.age} onChange={(v) => onChange('age', v)} min={1} max={120} />
        </Field>

        <Field label="⚧ Gender">
          <Select value={inputs.gender} onChange={(v) => onChange('gender', v)} options={GENDER_OPTIONS} />
        </Field>

        <Field label="💔 Chest Pain Type">
          <Select
            value={inputs.chestPain}
            onChange={(v) => onChange('chestPain', v)}
            options={CHEST_PAIN_OPTIONS}
          />
        </Field>

        <Field label="💓 Resting BP (mm Hg)">
          <RangeInput
            value={inputs.restingBP}
            onChange={(v) => onChange('restingBP', v)}
            min={80}
            max={200}
          />
        </Field>

        <Field label="🩸 Cholesterol (mg/dL)">
          <RangeInput
            value={inputs.cholesterol}
            onChange={(v) => onChange('cholesterol', v)}
            min={100}
            max={600}
          />
        </Field>

        <Field label="🍬 Fasting Blood Sugar > 120 mg/dL">
          <Select
            value={inputs.fastingBS}
            onChange={(v) => onChange('fastingBS', v)}
            options={FBS_OPTIONS}
          />
        </Field>

        <Field label="📈 Resting ECG">
          <Select
            value={inputs.restECG}
            onChange={(v) => onChange('restECG', v)}
            options={ECG_OPTIONS}
          />
        </Field>

        <Field label="💗 Max Heart Rate">
          <RangeInput
            value={inputs.maxHR}
            onChange={(v) => onChange('maxHR', v)}
            min={60}
            max={220}
          />
        </Field>

        <Field label="🏃 Exercise-Induced Angina">
          <Select
            value={inputs.exerciseAngina}
            onChange={(v) => onChange('exerciseAngina', v)}
            options={ANGINA_OPTIONS}
          />
        </Field>

        <Field label="📉 ST Depression">
          <RangeInput
            value={inputs.stDepression}
            onChange={(v) => onChange('stDepression', v)}
            min={0}
            max={10}
            step={0.1}
          />
        </Field>

        <Field label="📉 ST Slope">
          <Select
            value={inputs.stSlope}
            onChange={(v) => onChange('stSlope', v)}
            options={SLOPE_OPTIONS}
          />
        </Field>
      </div>

      <button
        className={styles.analyzeBtn}
        onClick={onAnalyze}
        disabled={loading}
      >
        {loading ? '⏳ Analyzing...' : '🚀 Generate Diagnostic Report'}
      </button>
    </div>
  );
}
