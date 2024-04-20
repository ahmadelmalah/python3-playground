def level1():
    x = 1

    def level2():
        y = 2

        def level3():
            z = 3
            print(x, y, z)

        level3()

    level2()


level1()
