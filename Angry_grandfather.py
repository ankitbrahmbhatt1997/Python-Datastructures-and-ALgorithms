def modInverse(a, m) : 
	m0 = m 
	y = 0
	x = 1
	
	if (m == 1) : 
		return 0
	while (a > 1) : 
		q = a // m 
		t = m 
		m = a % m 
		a = t 
		t = y 
		y = x - q * y 
		x = t 
	if (x < 0) : 
		x = x + m0 
	return x 
  
t = int(input())
while(t):
	t -= 1
	mod = 10**9 + 7
	n,m,k = map(int,input().split())
	m_raise_n = [1]
	m_m1 = [1]
	for i in range(n): 
		m_raise_n.append((m_raise_n[-1] * m) % mod)
		m_m1.append(((m - 1) * m_m1[-1])%mod)

	c = [1]
	for i in range(0, k-1):
		c.append((c[-1] * modInverse(i+1 , mod)*(n - i)) % mod)

	run = 0
	for i in range(0, k):	
		run = (run + (m_m1[n - i]*c[i])) % mod

	run = (m_raise_n[-1] + mod - run) % mod	
	# print run