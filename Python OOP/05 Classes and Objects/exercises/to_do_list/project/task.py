class Task:
    """
    Task("Make bed", "27/05/2020")
    print(task.change_name("Go to University"))
    print(task.change_due_date("28.05.2020"))
    task.add_comment("Don't forget laptop")
    task.edit_comment(0, "Don't forget laptop and notebook")
    """
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: list = []
        self.completed: bool = False


    def change_name(self, new_name: str) -> str:
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date:str) -> str:
        if new_date == self.due_date:
            return "Date cannot be the same."
        self.due_date =  new_date
        return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        try:
            self.comments[comment_number] = new_comment
        except IndexError:
            return "Cannot find comment."
        return ", ".join(comment for comment in self.comments)

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"