def exibir_grade():
    #so mostra os horarios que tem aula
    global dic_horarios
    divisor_linha = '+---------------+----------+----------+----------+----------+----------+----------+'
    linha_dia = '|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |'
    M1, M2, M3, M4, M5 = '| 08:00 - 08:55 |', '| 08:55 - 09:50 |', '| 10:00 - 10:55 |', '| 10:55 - 11:50 |', '| 12:00 - 12:55 |'
    T1, T2, T3, T4, T5, T6 = '| 12:55 - 13:50 |', '| 14:00 - 14:55 |', '| 14:55 - 15:50 |', '| 16:00 - 16:55 |', '| 16:55 - 17:50 |', '| 18:00 - 18:55 |'
    N1, N2, N3, N4 = '| 19:00 - 19:50 |', '| 19:50 - 20:40 |', '| 20:50 - 21:40 |', '| 21:40 - 22:30 |'
    print(divisor_linha)
    print(linha_dia)
    print(divisor_linha)
    lista_M = []
    lista_T = []
    lista_N = []
    for hora in dic_horarios: # como as chaves do dicionario sao todas Mx, Tx, ou Nx (1 <= x <= 6), divido esses horarios em lista para conseguir printar em ordem
        if 'M' in hora:
            lista_M.append(hora)
        elif 'T' in hora:
            lista_T.append(hora)
        elif 'N' in hora:
            lista_N.append(hora)
    lista_M.sort() # como todos os elementos das listas terao o primeiro caracter igual, o .sort() vai organizar de acordo com o codigo ASCII dos digitos, ou seja, vai estar em ordem crescente, de 1 a 6
    lista_T.sort()
    lista_N.sort()
    for hora in lista_M:
        if len(dic_horarios[hora]) != 0: # no caso de ter removido a materia e ter deixado a chave vazia, nao eh pra exibir esse horario, portanto o tamanho sempre tem que ser maior ou igual a 1
            if hora == 'M1':
                print(M1, end='')
                print_materias(hora)
            elif hora == 'M2':
                print(M2, end='')
                print_materias(hora)
            elif hora == 'M3':
                print(M3, end='')
                print_materias(hora)
            elif hora == 'M4':
                print(M4, end='')
                print_materias(hora)
            elif hora == 'M5':
                print(M5, end='')
                print_materias(hora)
            print(divisor_linha) # como o print_materias() n printa o divisor de linha (pra n ter que colocar mais argumentos na funcao), printo depois de qualquer ocasiao
    for hora in lista_T:
        if len(dic_horarios[hora]) != 0:
            if hora == 'T1':
                print(T1, end='')
                print_materias(hora)
            elif hora == 'T2':
                print(T2, end='')
                print_materias(hora)
            elif hora == 'T3':
                print(T3, end='')
                print_materias(hora)
            elif hora == 'T4':
                print(T4, end='')
                print_materias(hora)
            elif hora == 'T5':
                print(T5, end='')
                print_materias(hora)
            elif hora == 'T6':
                print(T6, end='')
                print_materias(hora)
            print(divisor_linha)    
    for hora in lista_N:
        if len(dic_horarios[hora]) != 0:
            if hora == 'N1':
                print(N1, end='')
                print_materias(hora)
            elif hora == 'N2':
                print(N2, end='')
                print_materias(hora)
            elif hora == 'N3':
                print(N3, end='')
                print_materias(hora)
            elif hora == 'N4':
                print(N4, end='')
                print_materias(hora)
            print(divisor_linha)
    return

def print_materias(horario):
    global dic_horarios
    nada = '          |'
    semana = [0]*6 # lista que mostrara as materias naquele horario na ordem Seg Ter Qua Qui Sex Sab, e quando n tem materia vai ter 0
    for par_dia_cod in dic_horarios[horario]:
        for dia in par_dia_cod[0]: # vai colocar cada materia em cada dia no respectivo lugar da semana
            semana[int(dia) - 2] = par_dia_cod[1] # indice eh o dia - 2 pq a gente quer que segunda seja o indice 0, e assim por diante, entao para que 2 + x = 0, x = -2
    for materias in semana:
        if materias == 0: # se na lista esta o elemento 0, significa que n mudou, portanto n tem materia naquele horario
            print(nada, end='')
        else:
            print(f' {materias} |', end='')
    print() # faz a quebra de linha, pq o end= padrao eh \n

def decodificar(horarios, codigo):
    erro = False
    lista_horarios = [] # lista em que em um indice tera a hora, e no outro tera uma lista com dias e codigo
    for hora in horarios:
        indice = 0
        if 'M' in hora:
            while hora[indice] != 'M': #Acha onde esta o turno pra separar a string
                indice += 1
            dias = list(hora[:indice]) # antes do M
            dias.sort() # pra regularizar todos os casos pra remover por igualdade depois
            horario = list(hora[indice + 1:]) # depois do M
            for hor in horario:
                # os parametros numericos dependem do horario
                if not (hor.isdigit() and int(hor) > 0 and int(hor) <= 5):
                    erro = True
                    break
                if ('M' + hor) not in lista_horarios: # se o horario n esta na lista
                    lista_horarios.append('M' + hor)
                    lista_horarios.append([dias, codigo])
                else: # se aquele horario ja existe na lista, adiciona os dias a lista de dias
                    index = lista_horarios.index('M' + hor)
                    datas = list(lista_horarios[index + 1][0])
                    for dia in dias:
                        datas.append(dia)
                    datas.sort() # pra regularizar todos os casos pra remover por igualdade depois
                    lista_horarios[index + 1][0] = list(datas) # substitui a lista ja existente pro python n zoar as outras listas que ja existem
        elif 'T' in hora:
            while hora[indice] != 'T': #Acha onde esta o turno pra separar a string
                indice += 1
            dias = list(hora[:indice]) # antes do T
            dias.sort() # pra regularizar todos os casos pra remover por igualdade depois
            horario = list(hora[indice + 1:]) # depois do T
            for hor in horario:
                if not (hor.isdigit() and int(hor) > 0 and int(hor) <= 6):
                    erro = True
                    break
                if ('T' + hor) not in lista_horarios:
                    lista_horarios.append('T' + hor)
                    lista_horarios.append([dias, codigo])
                else:
                    index = lista_horarios.index('T' + hor)
                    datas = list(lista_horarios[index + 1][0])
                    for dia in dias:
                        datas.append(dia)
                    datas.sort() # pra regularizar todos os casos pra remover por igualdade depois
                    lista_horarios[index + 1][0] = list(datas)
        elif 'N' in hora:
            while hora[indice] != 'N': #Acha onde esta o turno pra separar a string
                indice += 1
            dias = list(hora[:indice]) # antes do N
            dias.sort() # pra regularizar todos os casos pra remover por igualdade depois
            horario = list(hora[indice + 1:]) # depois do N
            for hor in horario:
                if not (hor.isdigit() and int(hor) > 0 and int(hor) <= 4):
                    erro = True
                    break
                if ('N' + hor) not in lista_horarios:
                    lista_horarios.append('N' + hor)
                    lista_horarios.append([dias, codigo])
                else:
                    index = lista_horarios.index('N' + hor)
                    datas = list(lista_horarios[index + 1][0])
                    for dia in dias:
                        datas.append(dia)
                    datas.sort() # pra regularizar todos os casos pra remover por igualdade depois
                    lista_horarios[index + 1][0] = list(datas)
        else:
            erro = True
    return lista_horarios, erro

comando = input()
dic_horarios = {} # dicionario onde chave = horario (ex: M5, 5° horario da manha), e os valores = lista de listas onde o primeiro elemento eh uma lista com os dias, e o segundo eh o codigo da materia
while comando != 'Hasta la vista, beibe!':
    if comando == '?':
        exibir_grade()
    else:
        erro = False # flag pra controlar se o comando sera invalido para mostrar depois
        operacao, codigo, *horarios = comando.split() # todos os comandos sao nesse formato
        horas, erro = decodificar(horarios, codigo) # decodifico antes de ver a operacao pq as duas vao precisar de uma lista que eu consiga comparar com os valores do dicionario, e vê se teve algum erro
        # e a lista tbm esta organizada em pares [horario, [dias, codigo]]
        if operacao == '+' and len(horarios) != 0:
            indice = 0
            while indice < len(horas) and not erro: # pra verificar todos os pares da lista do decodificar()
                if horas[indice] in dic_horarios: # se o horario ja esta guardado, precisa verificar se os dia batem
                    for par_dia_cod in dic_horarios[horas[indice]]: # verificar os dias de todas as materias salvas
                        for dia in par_dia_cod[0]:
                            if dia in horas[indice + 1][0]: # se algum dia eh igual, n da pra adicionar a materia
                                erro = True
                                break # se o algum dia nesse horario ja esta ocupado, eh um erro e n precisa verificar mais
                        if erro:
                            break # pra economizar tempo, se tem erro ja sai
                indice += 2 # aumenta em 2 pq quero verificar os pares da lista de decodificar()
            if not erro: # se n achou um erro, pode adicionar no dicionario
                indice = 0
                while indice < len(horas): 
                    if horas[indice] not in dic_horarios: # se o horario n existe no dicionario, cria uma nova chave
                        dic_horarios[horas[indice]] = [horas[indice + 1]]
                    else: # se tem, so adiciona os dias e codigo a lista que ja existe
                        dic_horarios[horas[indice]].append(horas[indice + 1])
                    indice += 2 # pra verificar os pares da lista
        elif operacao == '-' and len(horarios) != 0: # operacao -
            indice = 0
            while indice < len(horas) and not erro: # pra ver se existe a materia nos horarios e dias dados
                if horas[indice] not in dic_horarios: 
                    erro = True # se nem existe o horario dado no dicionario, ja ta errado
                else:
                    achou = False # flag pra controlar se, em algum dos elementos da lista na chave horario no dicionario, tem a codigo que ele quer
                    for par_dia_cod in dic_horarios[horas[indice]]:
                        if par_dia_cod[1] == horas[indice + 1][1]:
                            achou = True # codigos iguais
                            for dia in par_dia_cod[0]:
                                if dia not in horas[indice + 1][0]: # confirma se os dias guardados naquele horario pro codigo certo batem com os dias dados
                                    erro = True
                                    break
                        if erro:
                            break
                    if not achou: 
                        erro = True # se n tem o codigo naquele horario, ta errado
                indice += 2
            if not erro:
                indice = 0
                while indice < len(horas): # remove do horario os dias e codigo exatos que estao naquela lista
                    dic_horarios[horas[indice]].remove(horas[indice + 1])
                    indice += 2
        elif len(horarios) == 0:
            print("Nao foram fornecidos horarios: ", end="")
            erro = True
        else:
            print("Nenhum comando fornecido: ", end="")
            erro = True
        
        if erro:
            print(f'!({comando})')

    comando = input() # recebe outro comando e evita um loop infinito