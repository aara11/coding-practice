#include<bits/stdc++.h>
using namespace std;

int main(){
    int t,i,m,n,q,j,k;
    cin>>t;
    while(i<t)
    {
        long long ans=0;
        cin>>n>>m>>q;
        int mm[n];
        vector<int> count(n+1,0);
        for(j=0;j<m;j++){
            cin>>mm[j];
        }
        for(j=0;j<q;j++){
            cin>>k;
            count[k]++;
            ans+=(n/k);
        }
        for(j=0;j<m;j++){
            for(k=1;k<=sqrt(mm[j]);k++){
                if (mm[j]%k==0){
                    ans-=count[k];
                    if (k*k<mm[j])
                        ans-=count[(mm[j]/k)];
                }
            }
        }
        cout<<"Case #"<<++i<<": "<<ans<<endl;
    }
    return 0;
}