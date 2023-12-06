import json


def main():
    with open("a.json") as f:
        data1 = json.load(f)
    range_table1, new_data1 = data_to_range_table(data1)
    with open("c.json") as f:
        data2 = json.load(f)
    range_table2, new_data2 = data_to_range_table(data2)
    print("Ранжировка 1:", range_table1, "Ранжировка 2:",  range_table2, sep="\n\n")
    ans = agreed_cluster_range(range_table1, range_table2)
    print("Ядра провтиворечий:")
    for el in ans:
        print(new_data1[el[1]], new_data2[el[0]])

def data_to_range_table(data):
    range_dict = {}
    weight = 0
    for item in data:
        if isinstance(item, list):
            for el in item:
                range_dict[el] = weight
        else:
            range_dict[item] = weight
        weight += 1
    new_data = []
    for i in range(len(data)):
        if isinstance(data[i], list):
            new_data += [el for el in data[i]]
        else:
            new_data.append(data[i])
    new_data.sort()
    n = len(new_data)
    Y = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if range_dict[new_data[i]] <= range_dict[new_data[j]]:
                Y[i][j] = 1

    return Y, new_data


def matr_op(a, b, op):
    n = len(a)
    res = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(a[i][j] + b[i][j] if op == "+" else a[i][j] * b[i][j])
        res.append(l)
    return res

def agreed_cluster_range(A, B):
    A_T = list(map(list, zip(*A)))
    B_T = list(map(list, zip(*B)))
    AB = matr_op(A, B, "*")
    A_T_B_T = matr_op(A_T, B_T, "*")
    summ_matr = matr_op(AB, A_T_B_T, "+")

    ans = []
    for i in range(len(A)):
        for j in range(i):
            if summ_matr[i][j] == 0:
                ans.append((i, j))
    return ans


main()

