import styles from './Sidebar.module.css';

const TIPS = [
  '🥗 Maintain a healthy, balanced diet',
  '🏃 Exercise regularly (30 mins daily)',
  '📊 Monitor BP & cholesterol levels',
  '🚭 Avoid smoking & excessive alcohol',
  '🧘 Manage stress effectively',
];

export default function Sidebar() {
  return (
    <aside className={styles.sidebar}>
      <div className={styles.logo}>
        <span>👨‍⚕️</span>
        <span className={styles.logoText}>Patient Info</span>
      </div>

      <div className={styles.infoBox}>
        <p>📝 Fill patient details in the main panel to get AI-based cardiac risk assessment.</p>
      </div>

      <div className={styles.section}>
        <h3 className={styles.sectionTitle}>💡 Health Tips</h3>
        <ul className={styles.tipsList}>
          {TIPS.map((tip) => (
            <li key={tip} className={styles.tip}>
              {tip}
            </li>
          ))}
        </ul>
      </div>

      <div className={styles.footer}>
        🏆 Cardiac Risk Assessment v2.0
        <br />
        <span>AI-Powered Diagnostic Support</span>
      </div>
    </aside>
  );
}
