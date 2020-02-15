#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long t,tt,i,j,k;
    tt=0;
    cin>>t;
    while(tt<t)
    {
        long long n;
        cin>>n;
        vector<long long> t;
        vector<long long> s;
        vector<long long> r;
        for(i=0;i<2*n;i++)
        {
            cin>>k;
            t.push_back(k);
        }
        long long num_r=0, idx_r=0;
        for(i=0;i<2*n;i++)
        {
            if(num_r>0)
            {
                if(idx_r<num_r)
                {
                    if(r[idx_r]==t[i])
                    {
                        idx_r++;
                    }
                    else
                    {
                        s.push_back(t[i]);
                        r.push_back(t[i]*4/3);
                        num_r++;
                    }
                }
                else
                {
                    s.push_back(t[i]);
                    r.push_back(t[i]*4/3);
                    num_r++;
                }
            }
            else
            {
                s.push_back(t[i]);
                r.push_back(t[i]*4/3);
                num_r++;
            }
        }
        
        
        tt++;
        cout<<"Case #"<<tt<<": ";
        for(i=0;i<n;i++)
        {
            cout<<s[i]<<" ";
        }
        cout<<endl;
    }
}