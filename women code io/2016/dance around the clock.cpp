#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long t,tt,n,k,d,p;
    tt=0;
    cin>>t;
    while(tt<t)
    {

        cin>>d>>k>>n;
        long long l,r;
        l=k+1;
        r=k-1;
        if(k%2==0)
        {
            l-=(2*n);
            r-=(2*n);
            l=l%d;
            r=r%d;
        }
        else
        {
            l+=(2*n);
            r+=(2*n);
            l=l%d;
            r=r%d;
        }
        if(l<=0)
            l+=d;
        if(r<=0)
            r+=d;
        tt++;
        cout<<"Case #"<<tt<<": ";
        cout<<l<<" "<<r;
        cout<<endl;
    }
}
