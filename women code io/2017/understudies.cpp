#include<bits/stdc++.h> 
using namespace std; 
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        double a[2*n];
        for(int j=0;j<2*n;j++)
            cin>>a[j];
        sort(a,a+(2*n));
        double ans=1;
        for(int j=0;j<n;j++)
            ans*=(1-(a[j]*a[2*n-j-1]));
        cout<<"Case #"<<i<<": ";
        cout << fixed << setprecision(9)<<ans<<endl;
    }
}