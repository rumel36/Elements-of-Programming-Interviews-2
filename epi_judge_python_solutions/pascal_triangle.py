from test_framework import generic_test


def generate_pascal_triangle(n):

    result = [[1] * (i + 1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    print(result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
