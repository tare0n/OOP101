class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


list_of_tasks = ["купить лампочку", "поменять лампочку", "выбросить лампочку"]
todo_list = TodoList()
for task in list_of_tasks:
    todo_list.add_task(task)

print("\n".join(todo_list.tasks))