class block:
    """ This class is used to represent a time block
    ...
    Attributes
    ----------
    productive_mins : int
        states the number of productive minutes in a block

    break_mins : int
        states the number of break minutes in a block

    total_mins : int
        states the number of total minutes in a block

    task : str
        a task to be performed during the time block

    break_activity : str
        an activity to be performed during the break time

    """

    def __init__(self, productive_mins: int = 25, break_mins: int = 5, task: str = None, break_activity: str = None) -> None:
        """" constructor """
        # if break_mins is None:
        #     self.break_mins = 25
        self.break_mins = break_mins

        # if self.productive_mins is None:
        #     self.productive_mins = 5
        self.productive_mins = productive_mins
        self.total_mins = self.break_mins + self.productive_mins

        if task is not None:
            self.task = task

        if activity is not None:
            self.activity = activity

    def __str__(self):
        return ("block of {} productive and {} break minutes with"
                "the task: {} and break activity of {}").format(productive_mins, break_mins, task, break_activity)


class session:
        """ This class is used to represent a session of the application
        ...
        Attributes
        ----------
        num_of_hours : int
            states the number of hours within a session

        num_of_total_mins_in_block : int
            states the number of total minutes in a block which is used to determine the number of blocks needed in a session

        num_of_blocks : int
            states the number of blocks within a session

        block_list : List[block]
            a list of block objects within a session

        """

    def __init__(self, num_of_hours: int = 2, num_of_total_mins_in_block: int = 30) -> None:
        """ constructor initalizes a session with a list of blocks"""

        # if num_of_hours = None:
        #     num_of_hours = 2
        self.num_of_hours = num_of_hours
        self.num_of_total_mins_in_block = num_of_total_mins_in_block

        # create a list of blocks based on the number of hours and total minutes in a time block
        self.num_of_blocks = num_of_hours * 60 / num_of_total_mins_in_block
        self.block_list = [block() for i in num_of_blocks]

    def assign_task_to_block(self, block_index: int, task: str) -> None:
        """ assigns a task to a block"""
        # TODO:

    def complete_all_tasks(self) -> None:
        """ marks all the tasks as completed"""
        # TODO:

class task:
    """This class represents a task
    ...
    Attributes
    ----------
    detail : str
        states the detail of the task
    is_completed : bool
        states the status of the task: Incomplete or completed
    """
    def __init__(self, status: bool = false, detail: str) -> None:
        """constructor"""
        self.detail = detail
        self.status = status

    def complete_task(self) -> None:
        """marks a task as completed"""
        self.status = True

    def undo_completed_task(self) -> None:
        """marks a task as incomplete"""
        self.status = False

class file_management:
    """class responsible for file import/export operations
    # TODO: To be completed

    """
    # TODO: To be completed
