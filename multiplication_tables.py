def generateTable(n):

    with open(f"table{n}.txt", "w") as f:

        for i in range(1, 11):

            table = n * i

            f.write(f"{n} × {i} = {table}\n")


for i in range(2, 21):

    generateTable(i)
