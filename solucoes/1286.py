while True:
    n = int(input())

    if n == 0:
        break
    
    p = int(input())
    
    pedidos = []
    
    for i in range(n):
        tempo, pizzas = map(int, input().split())
        pedidos.append((tempo, pizzas))
    
    dp = [0] * (p + 1)
    
    for tempo, pizzas in pedidos:
        for j in range(p, pizzas - 1, -1):
            dp[j] = max(dp[j], dp[j - pizzas] + tempo)
    
    print(f"{dp[p]} min.")