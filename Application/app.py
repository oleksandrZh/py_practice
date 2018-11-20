#!Practice application
from Model import test_user as user
from Model import element
from Application.math_methods import *
from Application.str_methods import *

name = str()


# User = "Sergey"


def main():
    # user_var = set_user_name()
    #    print("name > " + name)
    #    print("name > " + set_user_name())
    #    print_user_name(user_var)
    #    print(user.set_def_user_name())
    new_element = element.Element(132)
    print("id: " + str(new_element.get_elemt_id()))
    element.Element.say_hello()
    print(plus(3, 2, 3, 10))
    print(minus(10, 3, 1, 2))

    print(count_words("Three simple word"))
    hokku = create_hokku("Test created", "for managers", "by QA")
    print(hokku)


def set_user_name():
    name = "Alex"
    return name


def print_user_name(name):
    print(name)


def math():
    print(7 / 3)
    print(round(7. / 3, 3))
    print(7 // 3)
    var = input("Enter value: ")
    if int(var) == 20:
        print("==")
        print("done")
    elif int(var) < 20:
        print("<")
        print("done")
    else:
        print(">")
        print("done")


main()
