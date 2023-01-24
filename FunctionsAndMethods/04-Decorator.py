def func(new_func):
    def funcc():
        print("Function started.")
        new_func()
        print("Function finished.")
    return funcc


def func2():
    print("Hello World")


def func3():
    def func4():
        print("Function4")
    return func4


def decoratorFunciton(func):
    def wrapperFunction():
        print("Wrapper started.")
        func()
        print("Wrapper finished.")
    return wrapperFunction


# ! We can call the function inside a another function too.
#decoratorFunc = decoratorFunciton(func2)
# decoratorFunc()

#! There is a shortcut here. We don't have to do confused steps, if we define the function "@decoratorFunc" pyhton will do same steps in background.
@decoratorFunciton
def func2():
    print("Hello World")


func2()
