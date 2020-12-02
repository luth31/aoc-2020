import os.path


def file_exists(path: str):
    if not os.path.isfile(path):
        print(f'Error: File {path} not found or not a file!')
        return False
    return True


def get_input_paths(path: str) -> (str, str):
    file_name = os.path.basename(path)[:-3]
    first_path = os.path.abspath(f'input/{file_name}_1.in')
    second_path = os.path.abspath(f'input/{file_name}_2.in')
    return first_path, second_path
