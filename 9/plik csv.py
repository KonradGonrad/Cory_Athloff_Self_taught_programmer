import csv

with open("Programista samouk\9 - Pliki\kkk.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["jeden",
                    "dwa",
                    "trzy"])
    write.writerow(["cztery",
                    "pięć",
                    "szesc"])
    
with open("Programista samouk\9 - Pliki\kkk.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))