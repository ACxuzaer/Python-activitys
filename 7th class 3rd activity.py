def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'ABC', 'V'], [2, 'pq', 'V'], [3, 'XYZ', 'VI'], [4, 'LVP', 'VI'], [5, 'COD', 'VII']]

print("\nOrignal list of lists:")
print(students)
print("\nConverted lists to a dictionary:")
print(test(students))