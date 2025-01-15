class Methods:

    def __init__(self, *args):
        if all(arg is None for arg in args):
            self.__mc = []

    def __str__(self):
        return "\n".join(
            f"{key}: {value}" for key, value in self.__dict__.items()
            if not key.startswith('_Methods__')
        )