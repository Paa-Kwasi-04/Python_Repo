from collections import defaultdict
import argparse
import json
import csv
import os


class StudentGradeManager:
    SUBJECTS = ['Math', 'Science']

    def __init__(self, csv_path: str | None = None):
        # single record store per manager instance
        self._records: list[dict] = []
        self.csv_path = csv_path
        if self.csv_path:
            self._ensure_csv_dir()
            if os.path.exists(self.csv_path):
                self._load_csv()

    def _ensure_csv_dir(self):
        d = os.path.dirname(os.path.abspath(self.csv_path))
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)

    def _load_csv(self):
        try:
            with open(self.csv_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        score = int(row.get('score', 0))
                    except ValueError:
                        continue
                    name = row.get('name', '').strip().capitalize()
                    subject = row.get('subject', '').strip().capitalize()
                    grade = row.get('grade') or self._grade_from_score(score)
                    self._records.append({
                        'name': name,
                        'subject': subject,
                        'score': score,
                        'grade': grade
                    })
        except FileNotFoundError:
            pass

    def _write_csv(self, path: str | None = None):
        path = path or self.csv_path
        if not path:
            return
        fieldnames = ['name', 'subject', 'score', 'grade']
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in self._records:
                writer.writerow({
                    'name': r['name'],
                    'subject': r['subject'],
                    'score': r['score'],
                    'grade': r['grade']
                })

    def add_student(self, name: str, subject: str, score: int):
        name = name.strip().capitalize()
        subject = subject.strip().capitalize()
        self._validate_subject(subject)
        self._validate_score(score)
        grade = self._grade_from_score(score)

        record = {
            'name': name,
            'subject': subject,
            'score': score,
            'grade': grade
        }
        self._records.append(record)
        # persist immediately if using CSV
        if self.csv_path:
            self._write_csv()
        return record

    def export_csv(self, path: str):
        """Write current records to a given CSV path (does not change default csv_path)."""
        self._ensure_csv_dir() if self.csv_path else None
        self._write_csv(path)

    def _validate_score(self, score: int):
        if not isinstance(score, int) or score < 0 or score > 100:
            raise ValueError('Score must be an integer between 0 and 100')

    def _validate_subject(self, subject: str):
        if subject not in self.SUBJECTS:
            raise ValueError(
                f"Subject must be one of: {', '.join(self.SUBJECTS)}")

    def _grade_from_score(self, score: int) -> str:
        if score >= 90:
            return 'A'
        if score >= 80:
            return 'B'
        if score >= 70:
            return 'C'
        if score >= 60:
            return 'D'
        return 'F'

    def view_all_records(self) -> list[dict]:
        # return copy to avoid external mutation
        return list(self._records)

    def student_report(self, name: str) -> dict:
        name = name.strip().capitalize()
        records = [r for r in self._records if r['name'] == name]
        if not records:
            return {'name': name, 'records': [], 'average': None}

        total = sum(r['score'] for r in records)
        avg = total / len(records)
        return {'name': name, 'records': records, 'average': avg}

    def class_report(self) -> dict:
        from collections import defaultdict
        by_name = defaultdict(list)
        for r in self._records:
            by_name[r['name']].append(r)

        class_summary = {}
        for name, recs in by_name.items():
            avg = sum(r['score'] for r in recs) / len(recs)
            class_summary[name] = {'records': recs, 'average': avg}

        overall_avg = None
        if self._records:
            overall_avg = sum(r['score']
                              for r in self._records) / len(self._records)

        return {'per_student': class_summary, 'overall_average': overall_avg}


def main():
    parser = argparse.ArgumentParser(
        description='Student Grade Manager (interactive)')
    parser.add_argument('--demo', action='store_true',
                        help='Preload demo records before starting the menu')

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_csv = os.path.join(script_dir, 'student_grades.csv')

    parser.add_argument('--csv', default=default_csv,
                        help='CSV file path to load/save records (defaults to student_grades.csv in script directory)')
    args = parser.parse_args()

    mgr = StudentGradeManager(csv_path=args.csv)

    if args.demo:
        mgr.add_student('Alice', 'Math', 92)
        mgr.add_student('Bob', 'Science', 78)
        mgr.add_student('Alice', 'Science', 85)
        print('Demo records loaded.')

    def print_menu():
        print("\nStudent Grade Manager")
        print("1) Add student")
        print("2) View all records")
        print("3) Student report")
        print("4) Class report")
        print("5) Export to CSV")
        print("6) Exit")

    try:
        while True:
            print_menu()
            choice = input("Choose an option (1-6): ").strip()

            if choice == '1':
                name = input("Student name: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue

                # show subject choices
                print("Available subjects:")
                for i, s in enumerate(mgr.SUBJECTS, start=1):
                    print(f"  {i}) {s}")
                subj_in = input("Subject (name or number): ").strip()
                if subj_in.isdigit():
                    idx = int(subj_in)
                    if 1 <= idx <= len(mgr.SUBJECTS):
                        subject = mgr.SUBJECTS[idx - 1]
                    else:
                        print("Invalid subject number.")
                        continue
                else:
                    subject = subj_in

                score_in = input("Score (0-100): ").strip()
                try:
                    score = int(score_in)
                except ValueError:
                    print("Score must be an integer.")
                    continue

                try:
                    record = mgr.add_student(name, subject, score)
                except ValueError as e:
                    print(f"Error: {e}")
                else:
                    print(
                        f"Added: {record['name']} - {record['subject']}: {record['score']} ({record['grade']})")

            elif choice == '2':
                records = mgr.view_all_records()
                if not records:
                    print("No records.")
                else:
                    print("\nAll records:")
                    for r in records:
                        print(
                            f"  {r['name']} - {r['subject']}: {r['score']} ({r['grade']})")

            elif choice == '3':
                name = input("Student name for report: ").strip()
                if not name:
                    print("Name cannot be empty.")
                    continue
                rpt = mgr.student_report(name)
                if not rpt['records']:
                    print(f"No records for {rpt['name']}.")
                else:
                    print(f"\nReport for {rpt['name']}:")
                    for r in rpt['records']:
                        print(f"  {r['subject']}: {r['score']} ({r['grade']})")
                    print(f"Average: {rpt['average']:.2f}")

            elif choice == '4':
                cr = mgr.class_report()
                print("\nClass report:")
                print(json.dumps(cr, indent=2))

            elif choice == '5':
                path = input(
                    "Export CSV path (leave empty to use --csv path): ").strip()
                if not path:
                    if not mgr.csv_path:
                        print("No default CSV configured. Provide a path.")
                        continue
                    path = mgr.csv_path
                try:
                    mgr.export_csv(path)
                    print(f"Exported to {path}")
                except Exception as e:
                    print(f"Failed to export: {e}")

            elif choice == '6':
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6.")
    except KeyboardInterrupt:
        print("\nInterrupted — exiting.")
    # end main


if __name__ == '__main__':
    main()
