from functions import *

todo_list = ToDoList(OrmConnection(db_name='todo.db').get_session())
menu = Menu(todo_list)
menu.run()
