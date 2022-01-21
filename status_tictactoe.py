def status(m):
    
    #percorrendo linhas
    for i in range(3):
        x = True
        o = True
        v = True
        for j in range(3):
            if m[i][j] != 'x':
                x = False
            if m[i][j] != 'o':
                o = False
            if m[i][j] != ' ':
                v = False
        if v == True:
            return 0
        if x == True:
            return 1
        if o == True:
            return 2
    
        #percorrendo colunas
    for i in range(3):
        x = True
        o = True
        for j in range(3):
            if m[j][i] != 'x':
                x = False
            if m[j][i] != 'o':
                o = False
        if x == True:
            return 1
        if o == True:
            return 2

    #percorrendo diagonais
    x = True
    o = True
    for i in range(3):
        if m[i][i] != 'x':
            x = False
        if m[i][i] != 'o':
            o = False
    if x == True:
        return 1
    if o == True:
        return 2

    x = True
    o = True
    for i in range(3):
        if m[2-i][i] != 'x':
            x = False
        if m[2-i][i] != 'o':
            o = False
    if x == True:
        return 1
    if o == True:
        return 2 
    
    p = True
    for i in range(3):
        for j in range(3):
            if m[i][j] == ' ':
                p = False
    if p == True:
        return 3
    return 4
