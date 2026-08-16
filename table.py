f = open("table.txt", "w")

for n in range(2, 20):
    for j in range(1, 11):
        table = j * n
        print(f"{n} × {j} = {table}")
        f.write(f"{n} × {j} = {table}\n")
    
    print()
    f.write("\n")

f.close()
