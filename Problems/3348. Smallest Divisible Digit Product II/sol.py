class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        t_factors = {2: 0, 3: 0, 5: 0, 7: 0}
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                t_factors[p] += 1
                temp //= p
        
        if temp > 1:
            return "-1"
            
        dp = [[float('inf')] * 30 for _ in range(48)]
        dp[0][0] = 0
        for i in range(48):
            for j in range(30):
                if dp[i][j] == float('inf'): continue
                for d in [2, 3, 4, 6, 8, 9]:
                    c2 = 0
                    if d in (2, 6): c2 = 1
                    elif d == 4: c2 = 2
                    elif d == 8: c2 = 3
                    
                    c3 = 0
                    if d in (3, 6): c3 = 1
                    elif d == 9: c3 = 2
                    
                    ni = min(47, i + c2)
                    nj = min(29, j + c3)
                    if dp[i][j] + 1 < dp[ni][nj]:
                        dp[ni][nj] = dp[i][j] + 1
                        
        def get_min_digits(req2, req3, req5, req7):
            r2, r3 = max(0, req2), max(0, req3)
            r5, r7 = max(0, req5), max(0, req7)
            return r5 + r7 + dp[r2][r3]
            
        c2, c3, c5, c7 = [0]*10, [0]*10, [0]*10, [0]*10
        for d in range(1, 10):
            temp_d = d
            while temp_d % 2 == 0: c2[d] += 1; temp_d //= 2
            while temp_d % 3 == 0: c3[d] += 1; temp_d //= 3
            while temp_d % 5 == 0: c5[d] += 1; temp_d //= 5
            while temp_d % 7 == 0: c7[d] += 1; temp_d //= 7

        n = len(num)
        z = n
        for i in range(n):
            if num[i] == '0':
                z = i
                break
                
        pref2, pref3, pref5, pref7 = [0]*(z + 1), [0]*(z + 1), [0]*(z + 1), [0]*(z + 1)
        for i in range(z):
            d = int(num[i])
            pref2[i+1] = pref2[i] + c2[d]
            pref3[i+1] = pref3[i] + c3[d]
            pref5[i+1] = pref5[i] + c5[d]
            pref7[i+1] = pref7[i] + c7[d]
            
        for i in range(z, -1, -1):
            if i == n:
                rem2 = max(0, t_factors[2] - pref2[n])
                rem3 = max(0, t_factors[3] - pref3[n])
                rem5 = max(0, t_factors[5] - pref5[n])
                rem7 = max(0, t_factors[7] - pref7[n])
                if get_min_digits(rem2, rem3, rem5, rem7) == 0:
                    return num
            else:
                for d in range(int(num[i]) + 1 if i < n else 1, 10):
                    if d == 0: continue
                    cur2 = pref2[i] + c2[d]
                    cur3 = pref3[i] + c3[d]
                    cur5 = pref5[i] + c5[d]
                    cur7 = pref7[i] + c7[d]
                    
                    rem2 = max(0, t_factors[2] - cur2)
                    rem3 = max(0, t_factors[3] - cur3)
                    rem5 = max(0, t_factors[5] - cur5)
                    rem7 = max(0, t_factors[7] - cur7)
                    
                    rem_len = n - 1 - i
                    
                    if get_min_digits(rem2, rem3, rem5, rem7) <= rem_len:
                        ans = [num[:i], str(d)]
                        
                        for pos in range(rem_len):
                            for nxt_d in range(1, 10):
                                nxt2, nxt3 = cur2 + c2[nxt_d], cur3 + c3[nxt_d]
                                nxt5, nxt7 = cur5 + c5[nxt_d], cur7 + c7[nxt_d]
                                
                                nxt_req2 = max(0, t_factors[2] - nxt2)
                                nxt_req3 = max(0, t_factors[3] - nxt3)
                                nxt_req5 = max(0, t_factors[5] - nxt5)
                                nxt_req7 = max(0, t_factors[7] - nxt7)
                                
                                if get_min_digits(nxt_req2, nxt_req3, nxt_req5, nxt_req7) <= rem_len - 1 - pos:
                                    ans.append(str(nxt_d))
                                    cur2, cur3, cur5, cur7 = nxt2, nxt3, nxt5, nxt7
                                    break
                        return "".join(ans)
                        
        L = max(n + 1, get_min_digits(t_factors[2], t_factors[3], t_factors[5], t_factors[7]))
        ans = []
        cur2 = cur3 = cur5 = cur7 = 0
        for pos in range(L):
            for nxt_d in range(1, 10):
                nxt2, nxt3 = cur2 + c2[nxt_d], cur3 + c3[nxt_d]
                nxt5, nxt7 = cur5 + c5[nxt_d], cur7 + c7[nxt_d]
                
                nxt_req2 = max(0, t_factors[2] - nxt2)
                nxt_req3 = max(0, t_factors[3] - nxt3)
                nxt_req5 = max(0, t_factors[5] - nxt5)
                nxt_req7 = max(0, t_factors[7] - nxt7)
                
                if get_min_digits(nxt_req2, nxt_req3, nxt_req5, nxt_req7) <= L - 1 - pos:
                    ans.append(str(nxt_d))
                    cur2, cur3, cur5, cur7 = nxt2, nxt3, nxt5, nxt7
                    break
                    
        return "".join(ans)