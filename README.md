# To-Do List
To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done in less time. It also helps you become more reliable for other people and save time for the best things in life.
The list supports:
- insertion
- deletion
- listing today's tasks
- listing week's tasks
- listing all tasks
- listing missed tasks - tasks whose deadline date is earlier than today's date

## Get started
- download the repository
- run the program in the command-line
```
To-Do_List > python main.py
```
### Sample usage

**Add task**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 5

Enter task
>Meet my friends
Enter deadline
>2020-04-28
The task has been added!
```
**Show today's tasks**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 1

Today 26 Apr:
Nothing to do!
```
**Show all tasks**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 3

All tasks:
1. Meet my friends. 28 Apr
2. Math homework. 30 Apr
3. Call my mom. 30 Apr
4. Order a new keyboard. 1 May

```
**Show Week's tasks**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 2

Sunday 26 Apr:
Nothing to do!

Monday 27 Apr:
Nothing to do!

Tuesday 28 Apr:
1. Meet my friends

Wednesday 29 Apr:
Nothing to do!

Thursday 30 Apr:
1. Math homework
2. Call my mom

Friday 1 May:
1. Order a new keyboard 

Saturday 2 May:
Nothing to do!
```
**Show missed tasks**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 4

Missed tasks:
1. Learn the for-loop. 19 Apr
```
**Delete task**
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 6

Choose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
> 1
The task has been deleted!
```
