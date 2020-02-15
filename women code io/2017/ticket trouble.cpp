#include<bits/stdc++.h>
using namespace std;

int main()
{
    long long t,tt=0,f,s,a,b,i,j;
    cin>>t;
    while(tt<t)
    {
        cin>>f>>s;
        vector<vector<bool> > arr( s , vector<bool> (s, false));
        for(i=0;i<f;i++)
        {
            cin>>a>>b;
            arr[a-1][b-1]=true;
            arr[b-1][a-1]=true;
        }
        long long max_=0;
        for(i=0;i<s;i++)
        {
            long long ct=0;
            for(j=0;j<s;j++)
            {
                if(arr[i][j])
                {
                    ct+=1;
                }
            }
            max_=max(max_,ct);
        }
        tt++;
        cout<<"Case #"<<tt<<": ";
        cout<<max_;
        cout<<endl;
    }
}