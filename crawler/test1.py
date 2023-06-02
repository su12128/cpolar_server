def show(*args):
    for item in args:
        print(item)
    return None

class test:
    def __init__(self) -> None:
        pass
    def run(*args):
        show(*args)


if __name__ == "__main__":
    test1=test()
    test.run(1,2,3)