from contextlib import contextmanager

# file = open('file.txt', 'r')
# try:
#     file.write('hello')
# finally:
#     file.close()


# # Using Context Manager:
# with open("file.txt", "r") as file:
#     file.write("hello")


class File:
    """
    # Custom context manager
    """

    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):  # with XXXX as f
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()


# with File("file.txt", "w") as f:
#     print("Inside")
#     f.write("hello")
#     raise Exception()


@contextmanager
def file(filename, method):
    print('Enter')
    file = open(filename, method)
    yield file
    file.close()
    print("Exit")


with file("text.txt", "w") as f:
    print("Inside")
    f.write("hello")
