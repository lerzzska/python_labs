def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    for i in mat:
        if len(i)!= len(mat[0]):
            raise ValueError
    return [list(i) for i in zip(*mat)]

print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([]))
try:
    print(transpose([[1,2],[3]]))
except ValueError:
    print('ValueError')


print('')


def row_sums(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    for i in mat:
        if len(i)!= len(mat[0]):
            raise ValueError
    return [sum(i) for i in mat]

print(row_sums([[1,2,3],[4,5,6]]))
print(row_sums([[-1,1],[10,-10]]))
print(row_sums([[0,0],[0,0]]))
try:
    print(row_sums([[1,2], [3]]))
except ValueError:
    print('ValueError')


print('')


def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError
    return [sum(i) for i in zip(*mat)]

print(col_sums([[1,2,3],[4,5,6]]))
print(col_sums([[-1,1],[10,-10]]))
print(col_sums([[0,0],[0,0]]))
try:
    print(col_sums([[1,2],[3]]))
except ValueError:
    print('ValueError')


    

