

Task_List = [

]


def Menu():
    print("Todo List Menu\n"
          "1. View Tasks\n"
          "2. Add a Task\n"
          "3. Remove a Task\n"
          "4. Exit ")


def Choice_Func():
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if not (0 < choice < 5):
                raise ValueError()
            break
        except ValueError:
            print('Invalid choice')

    return choice


def View_task():
    if not Task_List:
        print('No tasks in the list\n')
        return

    for id, task in enumerate(Task_List, start=1):
        print(f'{id}. {task}')


def Add_task():
    while True:
        try:
            new_task = input('Enter a new task: ').strip().capitalize()
            if new_task == '' or new_task.isnumeric():
                raise ValueError()

            break
        except ValueError:
            print('Invalid task!')

    Task_List.append(new_task)


def Remove_task():
    View_task()

    while True:

        try:
            deleted_task = int(input('Enter the task number: '))-1
            if not (0 < deleted_task <= len(Task_List)) or deleted_task == '':
                raise ValueError()
            break
        except ValueError:
            print('Invalid task number')

    Task_List.pop(deleted_task)


def main():
    while True:
        print()
        Menu()
        choice = Choice_Func()

        if choice == 1:
            View_task()
            continue
        elif choice == 2:
            Add_task()
            continue
        elif choice == 3:
            Remove_task()
            continue
        else:
            break


if __name__ == '__main__':
    main()
    print(f'Todo List Items: {len(Task_List)}')
