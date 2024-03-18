ch = input().split()
n = int(ch[0])
m = int(ch[1])

matrix = []

for _ in range(n): 
    l = [0 for _ in range(m)]
    matrix.append(l)

x = 0
y = 0

dx = 0   
dy = 1


matrix[0][0] = 1   # устанавливаем 1 в первую ячейку матрицы
count  = 2   # начинаем с 2, потомту что 1 уже поставили выше

while count <= n * m:
    
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and matrix[x + dx][y + dy] == 0:
        
        matrix[x + dx][y + dy] = count    # ставим в ячейку очередное число
        count += 1   # увеличиваем число, кот.потом поставим в след.итерации на 1
        x += dx   #меняем координаты x  и y
        y += dy
    else:
        if dy == 1:
            dy = 0
            dx = 1
        elif dx == 1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = 1
            
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end = ' ')
    print()    
        
        
        