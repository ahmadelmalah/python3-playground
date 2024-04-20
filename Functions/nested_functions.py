def level1():
    x = 1

    def level2():
        y = None

        def level3():
            nonlocal y
            y = 2
            z = 3
            print(x, y, z)

        level3()

    level2()


level1()
