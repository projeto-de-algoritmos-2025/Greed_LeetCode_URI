def resolve_caso():
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        return False
    
    l = int(input())
    
    k = int(input())
    
    comprimentos = list(map(int, input().split()))
    
    m_cm = m * 100
    n_cm = n * 100
    
    # Verificando se a largura nas 2 direções
    direcao1_possivel = n_cm % l == 0  
    direcao2_possivel = m_cm % l == 0  
    
    if not direcao1_possivel and not direcao2_possivel:
        print("impossivel")
        return True
    
    min_tabuas = float('inf')
    
    if direcao1_possivel:
        num_faixas = n_cm // l
        resultado = tentar_cobertura(comprimentos.copy(), m, num_faixas)
        if resultado != -1:
            min_tabuas = resultado
    
    if direcao2_possivel:
        num_faixas = m_cm // l
        resultado = tentar_cobertura(comprimentos.copy(), n, num_faixas)
        if resultado != -1:
            min_tabuas = min(min_tabuas, resultado)
    
    if min_tabuas == float('inf'):
        print("impossivel")
    else:
        print(min_tabuas)
    
    return True

def tentar_cobertura(comprimentos, comprimento_faixa, num_faixas):

    freq = {}
    for comp in comprimentos:
        freq[comp] = freq.get(comp, 0) + 1
    
    placas_exatas = min(freq.get(comprimento_faixa, 0), num_faixas)
    
    if comprimento_faixa in freq:
        freq[comprimento_faixa] -= placas_exatas
        if freq[comprimento_faixa] == 0:
            del freq[comprimento_faixa]
    
    faixas_restantes = num_faixas - placas_exatas
    
    if faixas_restantes == 0:
        return placas_exatas
    
    tabuas_disponiveis = []
    for comp, qtd in freq.items():
        tabuas_disponiveis.extend([comp] * qtd)
    
    tabuas_disponiveis.sort()
    
    inicio = 0
    fim = len(tabuas_disponiveis) - 1
    pares = []
    usado = [False] * len(tabuas_disponiveis)
    
    while inicio < fim:
        if usado[inicio]:
            inicio += 1
            continue
            
        if usado[fim]:
            fim -= 1
            continue
            
        soma = tabuas_disponiveis[inicio] + tabuas_disponiveis[fim]
        
        if soma == comprimento_faixa:
            pares.append((tabuas_disponiveis[inicio], tabuas_disponiveis[fim]))
            usado[inicio] = True
            usado[fim] = True
            inicio += 1
            fim -= 1
        elif soma < comprimento_faixa:
            inicio += 1
        else:
            fim -= 1
    
    if len(pares) < faixas_restantes:
        return -1
    
    return placas_exatas + 2 * faixas_restantes

while resolve_caso():
    pass