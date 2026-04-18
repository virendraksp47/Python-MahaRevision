def myfunc():
    print("This is my function")


if __name__ == "__main__":
    print("This is the main module")
    myfunc()
    print(__name__)
else:
    print("This is not the main module")
    print(__name__)