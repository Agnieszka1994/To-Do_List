from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __str__(self):
        return self.task


class OrmConnection:
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
        Base.metadata.create_all(self.engine)

        self.session = sessionmaker(bind=self.engine)()

    def get_session(self):
        return self.session


class ToDoList:
    def __init__(self, session):
        self.session = session

    def show_today_tasks(self):
        self._get_day_task(datetime.today(), today=True)

    def show_week_tasks(self):
        for i in range(7):
            self._get_day_task(datetime.today() + timedelta(days=i))

    def _get_day_task(self, day, today=False):
        tasks = self.session.query(Table).filter(Table.deadline == day.date()).all()
        if today:
            print(f'\nToday {day.strftime("%#d %b")}:')
        else:
            print(f'{day.strftime("%A %#d %b")}:')

        if tasks:
            for nr, task in enumerate(tasks, 1):
                print(f'{nr}. {task}')
        else:
            print('Nothing to do!')
        print()

    def show_missed_tasks(self):
        tasks = self.session.query(Table).filter(Table.deadline < datetime.today().date()).\
            order_by(Table.deadline).all()
        print('\nMissed tasks:')
        if tasks:
            self._print_tasks_with_date(tasks)
        else:
            print('Nothing is missed!\n')
        print()

    def show_all_tasks(self):
        tasks = self.session.query(Table).order_by(Table.deadline).all()
        print('\nAll tasks:')
        if tasks:
            self._print_tasks_with_date(tasks)
        else:
            print('Nothing to do!\n')
        print()

    @staticmethod
    def _print_tasks_with_date(tasks):
        for nr, task in enumerate(tasks, 1):
            print(f'{nr}. {task}. {task.deadline.strftime("%#d %b")}')

    def add_task(self):
        task = input('\nEnter task')
        deadline = datetime.strptime(input('Enter deadline'), '%Y-%m-%d')
        self.session.add(Table(task=task, deadline=deadline))
        self.session.commit()
        print('The task has been added!\n')

    def delete_task(self):
        tasks = self.session.query(Table).order_by(Table.deadline).all()
        if tasks:
            self._print_tasks_with_date(tasks)
            try:
                user_input = int(input('Choose the number of the task you want to delete:'))
            except TypeError:
                print('Task does not exist')
            else:
                specific_row = tasks[user_input - 1]
                self.session.delete(specific_row)
                self.session.commit()
                print('The task has been deleted!')
        else:
            print('Nothing to delete\n')
        print()

    @staticmethod
    def exit():
        print('Bye!')


class InputHandler:
    def __init__(self, todo_list):
        self.methods = {
            '1': todo_list.show_today_tasks,
            '2': todo_list.show_week_tasks,
            '3': todo_list.show_all_tasks,
            '4': todo_list.show_missed_tasks,
            '5': todo_list.add_task,
            '6': todo_list.delete_task,
            '0': todo_list.exit
        }

    def handle(self, user_input):
        if user_input not in self.methods.keys():
            raise KeyError(f"Method {user_input} not specified!")
        self.methods[user_input]()
        return user_input != '0'


class Menu:
    def __init__(self, todo_list):
        self.running = True
        self.handler = InputHandler(todo_list)

    def run(self):
        while self.running:
            self.show()
            self.running = self.handler.handle(input())

    @staticmethod
    def show():
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Missed tasks")
        print("5) Add task")
        print("6) Delete task")
        print("0) Exit")
