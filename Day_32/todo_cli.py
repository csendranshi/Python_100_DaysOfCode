import sys
import datetime

x = datetime.datetime.now()
date = str(x.strftime("%Y")) + "-" + str(x.strftime("%m")) + "-" + str(x.strftime("%d"))
out = sys.stdout
f = open("todo.txt", "a")


def add_task(task):
    # reads lines from 'todo_file' and stores result in a list-data
    with open('todo.txt', 'r') as todo_file:
        data = todo_file.readlines()
        # adds new task to list-data
        data.insert(0, task + "\n")

    with open('todo.txt', 'w') as todo_file:
        # writes the updated list-data to todo_file
        todo_file.writelines(data)
        print(f"Added todo: \"{task}\"")


def done_task(index):
    global date

    try:
        # checks if the task to be marked done exists and index is not zero
        with open('todo.txt', 'r') as todo_file:
            data = todo_file.readlines()
            if data[int(index) - 1] and (4 / int(index)):
                # adds the done task to the done_file
                with open('done.txt', 'a') as done_file:
                    done_file.write(f'x {date} {data[int(index) - 1]}')

        # deletes the marked task from todo_file
        with open('todo.txt', 'w') as todo_file:
            data.remove(data[int(index) - 1])
            todo_file.writelines(data)

        print(f"Marked todo #{index} as done.")

    except:
        print(f"Error: todo #{index} does not exist.")


def delete_task(index):
    # checks if the task to be deleted exists and index is not zero
    with open('todo.txt', 'r') as todo_file:
        data = todo_file.readlines()
        try:
            if data[int(index) - 1] and (4 / int(index)):
                pass

        except:
            print("Error: todo #" + str(index) + " does not exist. Nothing deleted.")

        else:
            # deletes the task from todo_file
            with open('todo.txt', 'w') as todo_file_write:
                data.remove(data[int(index) - 1])
                todo_file_write.writelines(data)
                print(f"Deleted todo #{index}")


def help_menu():
    res = """Usage :-
$ ./todo add \"todo item\"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""

    out.buffer.write(res.encode('utf8'))


def report():
    with open('todo.txt', 'r') as todo_file:
        pending = todo_file.readlines()
    with open('done.txt') as done_file:
        completed = done_file.readlines()
    res = date + " Pending : " + str(len(pending)) + " Completed : " + str(len(completed))
    out.write(res)


def ls():
    res = ""
    with open('todo.txt', 'r') as todo_file:
        pending = todo_file.readlines()
        # checks if todo_file has no tasks left
        if len(pending) == 0:
            print("There are no pending todos!")
        else:
            # prints tasks in order of newly added first
            for i in range(len(pending) - 1, -1, -1):
                res += '[{}] {}'.format(i + 1, pending[len(pending) - i - 1])
            out.buffer.write(res.encode('utf8'))


def main():
    # checks if no additional arguments are provided
    try:
        cmd = sys.argv[1]
    except:
        cmd = "help"

    if cmd == "help":
        help_menu()
    elif cmd == "add":
        try:
            add_task(sys.argv[2])
        except:
            out.write("Error: Missing todo string. Nothing added!")
    elif cmd == "done":
        try:
            done_task(int(sys.argv[2]))
        except:
            out.write("Error: Missing NUMBER for marking todo as done.")
    elif cmd == "del":
        try:
            delete_task(int(sys.argv[2]))
        except:
            out.write("Error: Missing NUMBER for deleting todo.")
    elif cmd == "report":
        report()
    elif cmd == "ls":
        ls()


main()
