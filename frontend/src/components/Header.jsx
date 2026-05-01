import styles from './Header.module.css';

export default function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.inner}>
        <span className={styles.icon}>🏥</span>
        <div>
          <h1 className={styles.title}>Cardiac Risk Assessment Dashboard</h1>
          <p className={styles.subtitle}>Advanced AI-Powered Diagnostic Support for Heart Health</p>
        </div>
        <span className={styles.badge}>v2.0</span>
      </div>
    </header>
  );
}
