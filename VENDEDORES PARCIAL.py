#Ejercicio 2
#Hacer un programa que lea las ternas de números. El primero representa un vendedor,
#el segundo a un mes y el tercero a un valor (los tres son enteros).
#1<=mes<=12; 1<=vend<=200. Termina cuando ingresan vendedor 0.
#El programa debe imprimir el mes en el cual cada vendedor vendio mas, el mes de
#mayores de ventas, el vendedor que mas vendio, el vendedor que mas vendio en cada mes y
#ventas totales.
meses = 12
def buscar(mat, f, elemento):
    for i in range(1, f+1):
        for j in range (1, meses + 1):
            if mat[i][j] == elemento:
                return j
    return -1
def sumames(mat, f):
    mesmayor = [0]
    r = 0
    for i in range(1, meses + 1):
        r = 0
        for j in range (1, f + 1):
            r = mat[j][i] + r
        mesmayor.append(r)
    return(mesmayor)
def sumavendido(mat, f):
    ventatotal = [0]
    for i in range (1, f + 1):
        l = 0
        for j in range (1, meses + 1):
            l = mat[i][j] + l
        ventatotal.append(l)
    return ventatotal
def mejorvendedorxmes(m, f):
    lista = [0]
    for i in range (1, meses + 1):
        lista2 = [0]
        for j in range (1, f + 1):
            lista2.append(m[j][i])
        w = lista2.index(max(lista2))
        lista.append(w)
    return lista
def ventastotales (m, f):
    ventastotales = []
    for i in range(1, f + 1):
        t = 0
        for j in range(1, meses + 1):
            t = m[i][j] + t
        ventastotales.append(t)
    total = sum(ventastotales)
    return total   
def programa():
    print("INGRESE LOS VENDEDORES")
    v = int(input("Ingrese el numero de vendedor (cero para terminar):"))
    f = 0
    while v != 0:
        f = f + 1
        v = int(input("Ingrese el numero de vendedor(cero para terminar):"))
    m = []
    for i in range (0, f+1):
        m.append([])
        for j in range (0, meses + 1):
            m[i].append(0)       
    cont2 = 0
    for i in range (1, f+1):
        cont2 = cont2 + 1
        m[i][0] = cont2
    cont3 = 0
    for i in range (1, meses + 1):
        cont3 = cont3 + 1
        m[0][i] = cont3
    print("EMPIEZA LA TEMPORADA DE VENTAS")
    vend = int(input("Ingrese el numero de vendedor (termina con cero):"))
    while vend != 0:
        mes = int(input("Ingrese el mes:"))
        venta = int(input("Ingrese la venta:"))
        m[vend][mes] = m[vend][mes] + venta
        vend = int(input("Ingrese el numero de vendedor (termina con cero):"))
    mejorm = [0] 
    for i in range (1,f+1):
        mventa = max(m[i])
        mesmejor = buscar(m, f, mventa)
        mejorm.append(mesmejor)
    posmejormes = (sumames(m, f)).index(max(sumames(m, f)))
    mejorvendedor = (sumavendido(m, f)).index(max(sumavendido(m,f)))
    mvendedorxmes = mejorvendedorxmes(m, f)
    guita = ventastotales(m, f)
    for i in range (0, f+1):
        print(m[i])
    for i in range (1, f+1):
        print("El mejor mes del vendedor ", i,"fue el:", mejorm[i])
    print("El mes en el que mas se vendio fue:", posmejormes)
    print("El mejor vendedor fue:", mejorvendedor)
    for i in range (1, meses + 1):
        print("El mejor vendedor del mes ", i,"es el:", mvendedorxmes[i])
    print("Las ventas totales fueron:", guita)
programa()       
        
        
        
    
    
    
    
    
    