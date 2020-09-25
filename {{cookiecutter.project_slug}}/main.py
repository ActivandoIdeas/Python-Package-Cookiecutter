# Hello name example


def print_hi(name):
    """Print dinamic name"""
    print(f'Hello, {name}')


if __name__ == '__main__':
    print_hi('{{cookiecutter.project_slug}}')
