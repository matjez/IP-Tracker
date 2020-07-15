path = "data/Ethernet/192.168.8.1.csv"
import csv

class Analyse:
    def __init__(self,path):
        with open(path) as f:
            self.data = csv.reader(f, delimiter=' ')
            for i in self.data:
                print(i)


    def print(self):
        for i in self.data:
            print(i)
x = [5,2,3,8,1,4,88,45,23,6,7]

x = sorted(x)

i = 1
while True:
    if i not in x:
        print(i)
        break
    i += 1
