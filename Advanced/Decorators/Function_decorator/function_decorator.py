# the decorator is used to assign a function inside function and extending the features and functionality of the function 


# for example

def dec(func):
    def new():
        print("hello")
        func()
        print("bye")
        
    return new


@dec
def main():
    print("kartik")

main()