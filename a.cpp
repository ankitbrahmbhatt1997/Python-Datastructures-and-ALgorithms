#include <bits/stdc++.h>
#define ll  long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sc second
#define fr first

using namespace std;

const int mod = 1e9+7;
const int N = 1e5+10;
int n,m,k;
ll fac[N];
ll inv[N];

ll pw(ll x, ll p){
	if(!p)
	    return 1;
	ll z = pw(x,p/2);
	z *= z;
	z %= mod;
	if(p%2 == 0)
	    return z;
	z *= x;
	z %= mod;
	return z;
}

ll c(ll x, ll y){
	ll res = fac[x]*inv[y];
	res %= mod;
	res *= inv[x-y];
	res %= mod;
	return res;
}

int main()  {
	fac[0] = inv[0] = 1;
	for(int i=1 ;i <N ;i ++){
	    fac[i] = fac[i-1]*i;
	    fac[i] %= mod;
	    inv[i] = pw(fac[i],mod-2);
	}

	int t;
	cin>>t;
	while(t--){
	    scanf("%d%d%d",&n,&m,&k);
	    ll res =0;
	    for(int i=k ; i <= n ;i ++){
	        res += (c(n,i) * pw(m-1,n-i))%mod;
	        res %= mod;
	    }
	    printf("%lld\n",res);
	}
	return 0;
}