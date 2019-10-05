
def solution(A):
    countries = list()

    for i in range(len(A)):
        for j in range(len(A[i])):
            country = A[i][j]
            if  A[i][j] :
                countries.append(country)
                A[i][j] = None
                find_country(A, i + 1, j, country)
                find_country(A, i - 1, j, country)
                find_country(A, i, j + 1, country)
                find_country(A, i, j - 1, country)
    print(countries)
    print('Number of countries: ', len(countries))
    return len(countries)


def find_country(A, i, j, country):

    try:
        if not A[i][j] :
            return
        elif A[i][j] == country:
            A[i][j] = None
        else:
            return
    except IndexError:
        return

    find_country(A, i + 1, j, country)
    find_country(A, i - 1, j, country)
    find_country(A, i, j + 1, country)
    find_country(A, i, j - 1, country)


if __name__ == "__main__":
    A = [[0 for x in range(3)] for y in range(7)]
    A[0][0] = 5
    A[0][1] = 4
    A[0][2] = 4
    A[1][0] = 4
    A[1][1] = 3
    A[1][2] = 4
    A[2][0] = 3
    A[2][1] = 2
    A[2][2] = 4
    A[3][0] = 2
    A[3][1] = 2
    A[3][2] = 2
    A[4][0] = 3
    A[4][1] = 3
    A[4][2] = 4
    A[5][0] = 1
    A[5][1] = 4
    A[5][2] = 4
    A[6][0] = 4
    A[6][1] = 1
    A[6][2] = 1

    solution(A)