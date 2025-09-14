import json
import os
# from datetime import datetime


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
    def menu(self) -> int:  # Fixed return type
        while True:
            try:
                print(
                    "1. Add Task\n"
                    "2. View Task\n"
                    "3. Mark Task as done\n"
                    "4. Delete Task\n"
                    "5. Exit")

                ans: int = int(input('Enter an option: '))
                if 0 < ans < 6:
                    return ans
                raise ValueError('Enter A valid Option from 1 - 5')
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


    def save_database(self,db: list) -> None:
        """Save database to file"""
        with open(self._FILEPATH, mode='w') as file:
            json.dump(db, file, indent=2)


    def View_task(self):
        db = self.load_database()

        if not db:
            print("No tasks found!")
            return

        for index, task in enumerate(db, start=1):
            status = "✓ Completed" if task['completed'] else "○ Pending"
            print(f'\nTask {index}: {status}')
            for key, value in task.items():
                if key != 'completed':  # Don't show completed separately since we show status
                    print(f'  {key}: {value}')
        print()


    def Mark_as_done(self):
        db = self.load_database()

        if not db:
            print("No tasks to mark as done!")
            return

        self.View_task()

        try:
            task_no: int = int(input('Which task do you want to mark as done: '))

            if 1 <= task_no <= len(db):
                if db[task_no-1]['completed']:
                    print("Task is already completed!")
                else:
                    db[task_no-1]['completed'] = True
                    self.save_database(db)
                    print("Task marked as completed!")
            else:
                print(f'Task number must be between 1-{len(db)}')
        except ValueError:
            print("Please enter a valid number")

        


    def Delete_task(self):
        db = self.load_database()

        if not db:
            print("No tasks to delete!")
            return

        self.View_task()

        try:
            task_no: int = int(input('Which task do you want to delete: '))

            if 1 <= task_no <= len(db):
                removed_task: dict = db.pop(task_no-1)
                self.save_database(db)
                print(f"Deleted task: '{removed_task['task']}'")
            else:
                print(f'Task number must be between 1-{len(db)}')
        except ValueError:
            print("Please enter a valid number")

        


    def Add_task(self):
        task: str = input('Enter a new task: ').strip()
        if not task:
            print("Task cannot be empty!")
            return

        due_date: str = input('Enter due date: ').strip()

        print("\nAvailable tags:")
        for index, tag in enumerate(self._TAGS, start=1):
            print(f'{index}: {tag}')

        while True:
            try:
                tag_choice: int = int(input('Enter tag number: '))
                if 1 <= tag_choice <= len(self._TAGS):
                    tag = self._TAGS[tag_choice-1]
                    break
            except ValueError:
                print("Invalid input,try again")
            

        new_task = {
            'task': task,
            'Due-Date': due_date,
            'tag': tag,
            'completed': False
        }

        db = self.load_database()
        db.append(new_task)
        self.save_database(db)

        print("Task added successfully!")



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
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
