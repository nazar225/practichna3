name = input("Введіт свє імя на англійському")

for name in name:
    if "C" in name:
        for i in range(7):
            row =  ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0:
                        row = " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 5:
                    if j == 4:
                        row = row + "*"
            print(row)

    if "D" in name:
        for i in range(7):
            row =  ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
            print(row)

    if "E" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                if i == 0 or i == 3 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 4:
                        row == row + "*"
            print(row)

    if "F" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                if i == 0:
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 3:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)
    if "G" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 0:
                        row = row + " "
                if i == 0 or i == 6:
                    if j == 1 or j == 2:
                        row == row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 2:
                        row = row  + " "
                if i == 0 or i == 6:
                    if j == 1 or j == 2:
                        row = row + "*"
                if i == 0 or i == 3 or i == 6:
                    if j == 3:
                        row = row + "*"
                if i == 1 or i == 3 or i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
            print(row)
    if "H" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)
    if "I" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)
    if "J" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 0:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 2:
                        row = row + "*"
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 6:
                    if j == 0 or j == 2:
                        row = row + "*"
            print(row)
    if "K" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 5:
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 1:
                        row = row + " "
            print(row)
    if "L" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                if i == 6:
                    if j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
            print(row)
    if "M" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 1 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 4 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 1 or j == 3:
                        row = row + "*"
                if i == 2:
                    if j == 2:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 2:
                        row = row + "*"
            print(row)
    if "N" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 1 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2:
                    if j == 1:
                        row = row + "*"
                if i == 2:
                    if j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 2:
                        row = row + "*"
                if i == 3:
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 4:
                    if j == 3:
                        row = row + "*"
            print(row)
    if "O" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 0:
                        row = row + " "
                if i == 0 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)
    if "P" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*" 
                if i == 1 or i == 2:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 0 or i == 3:
                    if j == 1 or j == 2 or j == 3:
                        row = row +"*"
                if i == 1 or i == 2:
                    if j == 4:
                        row = row + "*"
            print(row)
    if "Q" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                if i == 0 or i == 6:
                    if j == 0:
                        row = row + " "
                if i == 0:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 1 or j == 2:
                        row = row + " "
                if i == 6:
                    if j == 1 or j == 2 or j == 4:
                        row = row + "*"
                if i == 6:
                    if j == 3:
                        row = row + " "
            print(row)
    if "R" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*" 
                if i == 1 or i == 2:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 0 or i == 3:
                    if j == 1 or j == 2 or j == 3:
                        row = row +"*"
                if i == 1 or i == 2:
                    if j == 4:
                        row = row + "*"
                if i == 4 or i == 5 or i == 6:
                    if j == 4:
                        row = row + "*"
                if i == 4 or i == 5 or i == 6:
                    if j == 2:
                        row = row + " "
                if i == 5 or i == 6:
                    if j == 2:
                        row = row + " "
                if i == 6:
                    if j == 3:
                        row = row + " "
            print(row)
    if "S" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 3 or i == 6:
                   if j == 0:
                       row = row + " "
                if i == 0 or i == 3 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 0 or i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
                if i == 4 or i == 5:
                    if j == 0 or j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)
    if "T" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 4 or i == 5 or i == 6:
                    if j == 2:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 1:
                        row = row + " "
            print(row)
    if "U" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 4:
                        row = row + "*"
                if i == 6:
                    if j == 0:
                        row = row + " "
                if i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
            print(row)
    if "V" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 5:
                    if j == 0 or j == 2:
                        row = row + " "
                if i == 5:
                    if j == 1 or j == 3:
                        row = row + "*"
                if i == 6:
                    if j == 0 or j == 1:
                        row = row + " "
                if i == 6:
                    if j == 2:
                        row = row + "*"  
            print(row)
    if "W" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 2 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 3:
                    if j == 1 or j == 3:
                        row = row + " "
                if i == 4:
                    if j == 1 or j == 3:
                        row = row + "*"
                if i == 3:
                    if j == 2:
                        row = row + "*"
                if i == 4:
                    if j == 2:
                        row = row + " "
            print(row)
    if "X" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 0 or j == 2:
                        row = row + " "
                if i == 2 or i == 4:
                    if j == 1 or j == 3:
                        row = row + "*"
                if i == 3:
                    if j == 0 or j == 1:
                        row = row + " "
                if i == 3:
                    if j == 3:
                        row = row + "*"
            print(row)
    if "Y" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 0 or i == 1:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + " "
                if i == 2:
                    if j == 1 or j == 3:
                        row = row + "*"
                if i == 2:
                    if j == 2:
                        row = row + " "
                if i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 1:
                        row = row + " "
                if i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 2:
                        row = row + "*"
            print(row)
    if "Z" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 6:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
                if i == 1:
                    if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
                        row = row + " "
                if i == 2:
                    if j == 0 or j == 1 or j == 2:
                        row = row + " "
                if i == 3:
                    if j == 0 or j == 1:
                        row = row + " "
                if i == 4:
                    if j == 0:
                        row = row + " "
            print(row)
    if "B" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0:
                        row = row + "*"
                if i == 0 or i == 3 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 1 or i == 2 or i == 4 or i == 5:
                    if j == 4:
                        row = row + "*"
            print(row)
    if "A" in name:
        for i in range(7):
            row = ""
            for j in range(5):
                if i == 0:
                    if j == 0:
                        row = row + " "
                if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
                    if j == 0 or j == 4:
                        row = row + "*"
                if i == 1 or i == 2 or i == 4 or i == 5 or i == 6:
                    if j == 1 or j == 2 or j == 3:
                        row = row + " "
                if i == 0 or i == 3:
                    if j == 1 or j == 2 or j == 3:
                        row = row + "*"
            print(row)

