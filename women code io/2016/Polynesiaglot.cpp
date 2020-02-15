#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long t,tt,n,k,c,v,l,val;
    tt=0;
    n=1000000007;
    cin>>t;
    while(tt<t)
    {
        cin>>c>>v>>l;
        vector<long long> vv;
        vector<long long> cc;
        vv.push_back(v);
        cc.push_back(c);
        for(k=0;k<l-1;k++)
        {
            val=vv[k]*c;
            val=val%n;
            cc.push_back(val);
            val=(vv[k]+cc[k])*v;
            val=val%n;
            vv.push_back(val);
        }
        tt++;
        cout<<"Case #"<<tt<<": ";
        cout<<vv[l-1];
        cout<<endl;
    }
}
