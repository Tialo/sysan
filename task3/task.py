import csv
from math import log2

def get_file_data(path):
    with open(path, newline="") as csvfile:
        file_data = [[int(s) for s in line] for line in csv.reader(csvfile, delimiter=",", quotechar="|")]
    return file_data

def get_entropy(data):
    n = len(data)
    m = len(data[0])
    entropy = 0
    for i in range(n):
        for j in range(m):
            if data[i][j]:
                entropy -= data[i][j] * log2(data[i][j] / (n - 1)) / (n - 1)
    return entropy

def task():
    res = get_entropy(get_file_data("task3.csv"))
    print(res)
    return res

