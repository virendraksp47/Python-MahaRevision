def get():
    try:
        a=int(input("Hey, Enter a number: "))

    except Exception as e:
        print(e)

    finally:
        print("I am inside else")

get()

# important use in functions