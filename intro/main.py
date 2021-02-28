from helloworld import say_hello_world
from my_other_directory.greetings import say_hi


def main():
    res1 = say_hello_world()
    res2 = say_hi("Bob")
    return res1


if __name__ == "__main__":
    print(main())