import difflib
from colorama import Fore, Back, Style, init

#paste your output in the middle of the quotation marks
my_string = """""" 

# Initialize colorama for Windows compatibility
init(autoreset=True)

def compare_strings(string1, string2):
    lines1 = string1.splitlines()
    lines2 = string2.splitlines()
    d = difflib.Differ()
    diff = list(d.compare(lines1, lines2))

    if all(line.startswith('  ') for line in diff):
        return "The strings are identical."

    formatted_diff = []
    for line in diff:
        if line.startswith('- '):
            formatted_diff.append(format_line(line[2:], Fore.RED, "Removed"))
        elif line.startswith('+ '):
            formatted_diff.append(format_line(line[2:], Fore.GREEN, "Added"))
        elif line.startswith('? '):
            continue  # Skip the hint lines for simplicity
        else:
            formatted_diff.append(format_line(line[2:], Fore.BLUE, "Unchanged"))

    return "\n".join(formatted_diff)

def format_line(line, color, status):
    # Replace invisible whitespace characters with visible ones
    line = line.replace(' ', '·').replace('\t', '→')
    
    # Highlight trailing whitespace
    stripped = line.rstrip('·')
    if len(stripped) < len(line):
        trailing = line[len(stripped):]
        line = f"{stripped}{Back.YELLOW}{Fore.BLACK}{trailing}"
    
    # Format the line with status and color
    return f"{color}{status}: {line}{Style.RESET_ALL}"


original_string = """||=========================================================||
|| Welcome to the To-Do List App! Let's organise your day! ||
||=========================================================||

--- To-Do List App Features ---
0. Show Help Menu
1. Add Task
2. View Tasks
3. Remove Task
4. Switch Tasks Order
5. Quit

What would you like to do? (enter a command number of your choice 0-5):         
Please enter a valid number and try again!

What would you like to do? (enter a command number of your choice 0-5): 1dfg
Please enter a valid number and try again!

What would you like to do? (enter a command number of your choice 0-5): 8
Invalid choice of a number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 0

--- To-Do List App Features ---
0. Show Help Menu
1. Add Task
2. View Tasks
3. Remove Task
4. Switch Tasks Order
5. Quit

What would you like to do? (enter a command number of your choice 0-5): 2
There are no tasks in the list at the moment. Create one right now!

What would you like to do? (enter a command number of your choice 0-5): 3
There are no tasks in the list at the moment. Create one right now!

What would you like to do? (enter a command number of your choice 0-5): 1
Enter the task: 
Empty tasks are not supposed to appear in Your To-Do List! Try adding something else.

What would you like to do? (enter a command number of your choice 0-5): 1
Enter the task: first task
Task "first task" was successfully added to the list!

What would you like to do? (enter a command number of your choice 0-5): 2

Your To-Do List for today:
1) first task

What would you like to do? (enter a command number of your choice 0-5): 3

Your To-Do List for today:
1) first task

Enter the task number to remove: 
Invalid task number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 3

Your To-Do List for today:
1) first task

Enter the task number to remove: 1r
Invalid task number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 3

Your To-Do List for today: 
1) first task

Enter the task number to remove: 2
Invalid task number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 3

Your To-Do List for today:
1) first task

Enter the task number to remove: 1
Task "first task" was successfully removed from the list!

What would you like to do? (enter a command number of your choice 0-5): 2
There are no tasks in the list at the moment. Create one right now!

What would you like to do? (enter a command number of your choice 0-5): 4
There are no tasks in the list at the moment. Create one right now!

What would you like to do? (enter a command number of your choice 0-5): 1      
Enter the task: first task
Task "first task" was successfully added to the list!

What would you like to do? (enter a command number of your choice 0-5): 4

Your To-Do List for today:
1) first task

There is no point in switching when there is only one task in the list! Please, try something else.

What would you like to do? (enter a command number of your choice 0-5): 1
Enter the task: second task
Task "second task" was successfully added to the list!

What would you like to do? (enter a command number of your choice 0-5): 4

Your To-Do List for today:
1) first task
2) second task

Enter the first task number: 
Invalid task number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 4

Your To-Do List for today:
1) first task
2) second task

Enter the first task number: 1
Enter the second task number: 0
Invalid task number. Please try again.

What would you like to do? (enter a command number of your choice 0-5): 4

Your To-Do List for today:
1) first task
2) second task

Enter the first task number: 1
Enter the second task number: 1
There is no point in switching the task with itself! Please, try something else.

What would you like to do? (enter a command number of your choice 0-5): 4

Your To-Do List for today:
1) first task
2) second task

Enter the first task number: 1
Enter the second task number: 2
Tasks' positions were successfully switched!

What would you like to do? (enter a command number of your choice 0-5): 2

Your To-Do List for today:
1) second task
2) first task

What would you like to do? (enter a command number of your choice 0-5): 1
Enter the task: third task
Task "third task" was successfully added to the list!

What would you like to do? (enter a command number of your choice 0-5): 3

Your To-Do List for today:
1) second task
2) first task
3) third task

Enter the task number to remove: 2
Task "first task" was successfully removed from the list!

What would you like to do? (enter a command number of your choice 0-5): 2

Your To-Do List for today:
1) second task
2) third task

What would you like to do? (enter a command number of your choice 0-5): 5

Thank you for using the To-Do List App. Goodbye!"""

result = compare_strings(original_string, my_string)
print(result)
