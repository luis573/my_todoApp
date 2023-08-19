##############################com funções
FILEPATH='todos.txt'
def get_todos(filepath=FILEPATH):
    """Read a text file return a list with the todos in the file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a todos item in the list to a text files."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print('Hello from functions')
