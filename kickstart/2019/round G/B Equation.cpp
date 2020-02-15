#include<bits/stdc++.h>
using namespace std;

vector<long long> fac;
fac.push_back(1);
for(int kk=0;kk<50;kk++)
    fac.push_back(fac[-1]*2);

bool getval(int l,vector<boolean> ans, vector<int> ones,long long m,long long n)
{
if(m<0)
	return false;
if(l==0)
	return true;
if(2*ones[l-1] >= n)
{
m-=(fac[l-1]*ones[l-1]);
ans[l-1]=true;
return getval(l-1,ans,ones,m,n);
}
ans[l-1]=true;
if( getval(l-1,ans,ones,m-(fac[l-1]*ones[l-1]),n))
	return true;
ans[l-1]=false;
return getval(l-1,ans,ones,m-(fac[l-1]*(n-ones[l-1])),n);
}

int main(){
    long long t,n,m,final;
    cin>>t;
    int j,i,l;
    while(i<t)
    {
        cin>>n>>m;
        long long a[n];
        for(i=0;i<n;i++)
            cin>>a[i];
        boolean flag=true;
        vector<int> ones(51,0);
        l=0;
        for(i=0;i<n;i++)
        {
            j=0;
            while(a[i]>0)
            {
                if (a[i]%2==1)
                    ones[j]+=1;
                a[i]=a[i]/2;
                j++;
            }
            if (j>l)
	            l=j;
        }
        vector<boolean> ans(51,false);
        bool status = getval(l,ans,ones,m,n);
        if(status)
        {
            final=0;
            for(i=0;i<51;i++)
            {
                if (ans[i])
                    final+=fac[i];
            }
        }
        else
            final=-1;
        cout<<"Case #"<<++i<<": "<<final<<endl;
    }
    return 0;
}