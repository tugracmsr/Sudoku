import Sudoku
while True:
    print("Choose An Action")
    print("     1. Solve Sudoku")
    print("     2. Generate Sudoku")
    a = input(">")
    if a == "1":
        print("Write Numbers")
        numbers = input(">")
        grid = make_grid(numbers)
        solve()
        break
    elif a == "2":
        while True:
            print("Choose Level of Difficulty")
            print("     1. Beginner")
            print("     2. Intermediate")
            print("     3. Advanced")
            a = input(">")
            if a=="0":
                generate(35)
                break
            elif a=="2":
                generate(20)
                break
            elif a=="3":
                generate(8)
                break
        break
