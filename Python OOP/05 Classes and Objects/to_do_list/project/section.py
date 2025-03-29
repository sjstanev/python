from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []   # contain list of `Task` Objects

    def add_task(self, new_task: Task) -> str:

        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        # if task_name not in self.tasks:
        #     return f"Could not find task with the name {task_name}"
        # if task_name in self.tasks:
        #     index = self.tasks.index(task_name)
        #     self.tasks[index].completed = True
        #     return f"Completed task {task_name}"

        # This can be done with generator
        # loop through self.tasks list and check for the object's name(Task.name) equal to `task_name`
        # if find set the t = Object with name == task_name
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = 0
        for task in self.tasks:
            if task.completed:
                completed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {completed_tasks} tasks."

    def view_section(self):
        tasks_details = '\n'.join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_details}"
