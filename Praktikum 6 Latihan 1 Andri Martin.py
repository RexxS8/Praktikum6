def average(x = "0", t = 0, v = 0):
    while (x != ""):
        x = input("Masukkan Nilai: ")
        v += 1
        if(x == ""):
            if(v == 1):
                return 0
            else:
                return t/(v - 1)
        elif (x == "A"):
            print("Nilai = 4")
            t += 4
        elif (x == "A-"):
            print("Nilai = 3.75")
            t += 3.75
        elif (x == "B+"):
            print("Nilai = 3.25")
            t += 3.25
        elif (x == "B"):
            print("Nilai = 3")
            t += 3
        elif (x == "B-"):
            print("Nilai = 2.75")
            t += 2.75
        elif (x == "C+"):
            print("Nilai = 2.5")
            t += 2.5
        elif (x == "C"):
            print("Nilai = 2")
            t += 2
        elif (x == "C-"):
            print("Nilai = 1.75")
            t += 1.75
        elif (x == "D"):
            print("Nilai = 1.5")
            t += 1.5
        elif (x == "E"):
            print("Nilai = 1.25")
            t += 1.25
        else:
            x = 0
            
c = average()
print("Nilai Rata-Ratanya Adalah %0.2f " % c)