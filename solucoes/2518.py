class Solution:
    def countPartitions(self, nums, k):
        MOD = 10 ** 9 + 7
        soma_total = sum(nums)
        n = len(nums)
        if soma_total < 2 * k:
            return 0
        dp = [0] * k
        dp[0] = 1
        for numero in nums:
            for soma_atual in range(k - 1, numero - 1, -1):
                dp[soma_atual] = (dp[soma_atual] + dp[soma_atual - numero]) % MOD
        subconjuntos_ruins = sum(dp) % MOD
        total_de_particoes = pow(2, n, MOD)
        particoes_validas = (total_de_particoes - 2 * subconjuntos_ruins + MOD) % MOD
        return particoes_validas