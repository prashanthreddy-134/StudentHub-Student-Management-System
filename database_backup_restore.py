
import sqlite3
from pathlib import Path
from datetime import datetime

# Original database
SOURCE_DB = Path("students.db")

# Backup folder
BACKUP_DIR = Path("backups")
BACKUP_DIR.mkdir(exist_ok=True)

# Separate restoration test database
RESTORE_DB = Path("students_restore_test.db")

def check_database(db_path):
    """Check database integrity and count student records."""
    with sqlite3.connect(str(db_path)) as conn:
        integrity = conn.execute(
            "PRAGMA integrity_check"
        ).fetchone()[0]

        count = conn.execute(
            "SELECT COUNT(*) FROM students"
        ).fetchone()[0]

    return integrity, count


def create_backup():
    if not SOURCE_DB.exists():
        raise FileNotFoundError("students.db not found")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"students_backup_{timestamp}.db"

    # SQLite online backup API
    with sqlite3.connect(str(SOURCE_DB)) as source:
        with sqlite3.connect(str(backup_path)) as destination:
            source.backup(destination)

    integrity, count = check_database(backup_path)

    print("\n--- BACKUP RESULTS ---")
    print("Backup file:", backup_path)
    print("Backup size:", backup_path.stat().st_size, "bytes")
    print("Student records:", count)
    print("Integrity check:", integrity)

    if integrity != "ok":
        raise RuntimeError("Backup integrity check failed")

    return backup_path, count


def restore_test(backup_path, expected_count):
    # Restore into a separate test database.
    if RESTORE_DB.exists():
        RESTORE_DB.unlink()

    with sqlite3.connect(str(backup_path)) as source:
        with sqlite3.connect(str(RESTORE_DB)) as destination:
            source.backup(destination)

    integrity, restored_count = check_database(RESTORE_DB)

    print("\n--- RESTORE RESULTS ---")
    print("Restored database:", RESTORE_DB)
    print("Restored records:", restored_count)
    print("Integrity check:", integrity)

    if integrity != "ok" or restored_count != expected_count:
        raise RuntimeError("Restore verification failed")

    print("\nSUCCESS: Backup and restore verification passed.")


if __name__ == "__main__":
    backup_file, original_count = create_backup()
    restore_test(backup_file, original_count)
