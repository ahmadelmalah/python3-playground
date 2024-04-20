try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nah, you can't divide by zero!")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
