it_works = True


def magicspiral(N):
    # n - размерность матрицы n x n
    # mat - результирующая матрица
    # st - текущее значение-счетчик для записи в матрицу
    # m - коеффициент, используемый для заполнения верхней
    # матрицы последующих витков, т.к. одномерные матрицы
    # следующих витков имеют меньше значений
    n = int(N)
    mat = [[0] * n for i in range(n)]
    st, m = 1, 0
    # Заранее присваиваю значение центральному элементу
    # матрицы
    mat[n // 2][n // 2] = n * n
    for v in range(n // 2):
        # Заполнение верхней горизонтальной матрицы
        for i in range(n - m):
            mat[v][i + v] = st
            st += 1
            # i+=1
        # Заполнение правой вертикальной матрицы
        for i in range(v + 1, n - v):
            mat[i][-v - 1] = st
            st += 1
            # i+=1
        # Заполнение нижней горизонтальной матрицы
        for i in range(v + 1, n - v):
            mat[-v - 1][-i - 1] = st
            st += 1
            # i+=1
        # Заполнение левой вертикальной матрицы
        for i in range(v + 1, n - (v + 1)):
            mat[-i - 1][v] = st
            st += 1
            # i+=1
        # v+=1
        m += 2
    # Вывод результата на экран
    for i in mat:
        print(*i)


def normalarray(string):
    if ((int(string) >= 4) & (int(string) <= 1000)):
        pass
    else:
        print("Введите число, соответствующее условию задачи.")

    N = int(string)
    add = 1
    mas = []
    for i in range(N):
        mas.append([])
        for j in range(N):
            mas[i].append(add)
            add += 1
    print(mas)


while it_works:
    print("Введите число N, которое больше или равно 4, но меньше или равно 1000.")
    print("4<=N<=1000")
    print()
    string = input()

    print()

    print("Введите 1, если хотите магическую спираль и 0, если хотите увидеть обычное представление массива.")
    switch = input()
    if (switch == str(1)):
        print()
        magicspiral(string)
        print()
    elif (switch == str(0)):
        print()
        normalarray(string)
    else:
        it_works = False
        print()
        print("Введено некорректное значение.")

    print()

