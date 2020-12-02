import os.path


def file_exists(path: str):
    if not os.path.isfile(path):
        print(f'Error: File {path} not found or not a file!')
        return False
    return True


def get_input_path(path: str) -> str:
    filename = os.path.basename(path)[:-3]
    path = os.path.abspath(f'input/{filename}_1.in')
    return path
