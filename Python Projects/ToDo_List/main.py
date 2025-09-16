import json
import os
from datetime import datetime
import re


class TODO:
    def __init__(self):
        self._FILEPATH: str = 'database.json'
        self._TAGS: list = [
            'Personal',
            'Work',
            'School',
            'Shopping'
        ]
        self.OBJ: list = ['task', 'Due-Date', 'tag', 'completed']
        self.date_format = "%d/%m/%Y"

    def menu(self) -> int:  # Fixed return type
        while True:
            try:
                print(
                    "1. Add Task\n"
                    "2. View Task\n"
                    "3. Mark Task as done\n"
                    "4. Delete Task\n"
                    "5. Filter Search\n"
                    "6. Task Status\n"
                    "7. Exit")

                ans: int = int(input('Enter an option: '))
                if 0 < ans < 8:
                    return ans
                raise ValueError('Enter A valid Option from 1 - 7')
            except Exception as e:
                print(e)

    def load_database(self) -> list:
        """Load database, create if doesn't exist"""
        if os.path.exists(self._FILEPATH):
            try:
                with open(self._FILEPATH, mode='r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Database corrupted, starting fresh")
                return []
        else:
            print(f'{self._FILEPATH} doesn\'t exist, creating new database')
            return []

    def save_database(self, db: list) -> None:
        """Save database to file"""
        with open(self._FILEPATH, mode='w') as file:
            json.dump(db, file, indent=2)

    def View_task(self):
        today = datetime.now().date()
        db = self.load_database()

        if not db:
            print("No tasks found!")
            return

        for index, task in enumerate(db, start=1):
            task_date = datetime.strptime(task['Due-Date'], self.date_format).date()
            if task_date < today and not task['completed']:
                status = 'Overdue'
            else:
                status = "✓ Completed" if task['completed'] else "○ Pending"
            
            print(f'\nTask {index}: {status}')
            for key, value in task.items():
                if key != 'completed':
                    print(f'  {key}: {value}')
        print()

    def Mark_as_done(self):
        db = self.load_database()

        if not db:
            print("No tasks to mark as done!")
            return

        self.View_task()

        try:
            task_no: int = int(
                input('Which task do you want to mark as done: '))

            if 1 <= task_no <= len(db):
                if db[task_no-1]['completed']:
                    print("Task is already completed!")
                else:
                    db[task_no-1]['completed'] = True
                    self.save_database(db)
                    print("Task marked as completed!")
                    return
            else:
                raise ValueError(f'Task number must be between 1-{len(db)}')
        except Exception as e:
            print(e)

    def Delete_task(self):
        db = self.load_database()

        if not db:
            print("No tasks to delete!")
            return

        self.View_task()

        while True:
            try:
                task_no: int = int(input('Which task do you want to delete: '))

                if 1 <= task_no <= len(db):
                    removed_task: dict = db.pop(task_no-1)
                    self.save_database(db)
                    print(f"Deleted task: '{removed_task['task']}'")
                    return
                else:
                    raise ValueError(
                        f'Task number must be between 1-{len(db)}')
            except Exception as e:
                print(e)

    def enter_task(self)->str:
        while True:
            try:
                task: str = input('Enter a new task: ').strip()
                if not task or task.isdigit():
                    raise ValueError('Invalid task')
                return task
            except Exception as e:
                print(e)
    
    def enter_date(self)->str:
        while True:
            try: 
                date: str = input('Enter due date (dd/mm/yyyy): ').strip()
                due_date = self.validate_and_format_date(date)
                if due_date:
                    return due_date
                else: 
                    raise ValueError('Wrong date or date format')
            except Exception as e:
                print(e)
    def enter_tag(self)->str:
        while True:
            try:
                tag_choice: int = int(input('Enter tag number: '))
                if 1 <= tag_choice <= len(self._TAGS):
                    tag = self._TAGS[tag_choice-1]
                    return tag
            except ValueError:
                print("Invalid input,try again")

    def Add_task(self):
        task = self.enter_task()
        due_date = self.enter_date()

        print("\nAvailable tags:")
        for index, tag in enumerate(self._TAGS, start=1):
            print(f'{index}: {tag}')

        tag = self.enter_tag()

        new_task = {
            self.OBJ[0]: task,
            self.OBJ[1]: due_date,
            self.OBJ[2]: tag,
            self.OBJ[3]: False
        }

        db = self.load_database()
        db.append(new_task)
        self.save_database(db)

        print("Task added successfully!")

    def Search(self) -> list:
        db = self.load_database()
        db_task: list = [task['task']for task in db]

        search: str = input('What are you searching for: ').lower().strip()
        for index, task_des in enumerate(db_task):
            if search in task_des.lower():
                return db[index]
        return None

    def Status(self):
        db = self.load_database()
        db_status: list = [task['completed']for task in db]
        db_len: int = len(db_status)
        true_count: int = sum(db_status)

        return true_count, db_len
    
    def validate_and_format_date(self, date_string):

        date_formats = {
            r"^\d{2}/\d{2}/\d{4}$": "%d/%m/%Y",  # DD/MM/YYYY
            r"^\d{2}-\d{2}-\d{4}$": "%d-%m-%Y",  # DD-MM-YYYY
            r"^\d{4}-\d{2}-\d{2}$": "%Y-%m-%d",  # YYYY-MM-DD (ISO 8601)
            r"^\d{1,2}/\d{1,2}/\d{4}$": "%m/%d/%Y",  # M/D/YYYY (No leading zeros)
            r"^\d{1,2}\s[A-Z][a-z]{2}\s\d{4}$": "%d %b %Y",  # D Mon YYYY
            r"^[A-Z][a-z]{2}\s\d{1,2},\s\d{4}$": "%b %d, %Y"  # Mon D, YYYY
        }

        for pattern, fmt_code in date_formats.items():
            if re.fullmatch(pattern, date_string):
                try:
                    date_object = datetime.strptime(date_string, fmt_code)
                    return date_object.strftime(self.date_format)
                except ValueError:
                    continue

        return None


def main():
    todo_list = TODO()
    while True:
        choice = todo_list.menu()

        if choice == 1:
            todo_list.Add_task()
        elif choice == 2:
            todo_list.View_task()
            input("Press Enter to continue...")
        elif choice == 3:
            todo_list.Mark_as_done()
        elif choice == 4:
            todo_list.Delete_task()
        elif choice == 5:
            search = todo_list.Search()
            if search:
                for key, value in search.items():
                    print(f"{key}:{value}")
            else:
                print('Task not found')
        elif choice == 6:
            true_count, length = todo_list.Status()
            print(f'{true_count} task completed,{length-true_count} task pending')
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
