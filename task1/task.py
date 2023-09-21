import csv


if __name__ == '__main__':
    path, x, y = input().split()
    with open(path, newline="") as csvfile:
        file_data = list(csv.reader(csvfile, delimiter=",", quotechar='|'))
    print(file_data[int(x)][int(y)])
