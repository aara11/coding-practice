#include<bits/stdc++.h>
#include <iomanip>
using namespace std;
int main()
{
    long long t,i=0,k,j;
    cin>>t;
    vector< pair <int, int> > data;
    int rr=1,cc,r,c;
    double value;
    while(i<t)
    {
        cin>>r>>c;
        data.push_back(make_pair(abs(r),abs(c)));
        rr=max(rr,abs(r));
        rr=max(rr,abs(c));
        //cout<<rr<<" ";
        i++;
    }

    vector<vector<double> > vec(rr+1);
    for(i=0;i<=rr;i++)
        vec[i] = vector<double>(rr+1);
    vec[0][0]=0.0;
    vec[0][1]=3.0;
    vec[1][0]=3.0;
    vec[1][1]=4.0;
    for(i=2;i<=rr;i++)
    {
        value=(6+(2*vec[0][i-1])+vec[1][i-1])/3;

        vec[0][i]=value;
        value = 1+((vec[0][i]+vec[1][i-1])/2);
        vec[1][i]=value;
    }
    for(i=2;i<=rr;i++)
    {
        for(j=0;j<=rr;j++)
        {
            if(i==j)
            {
                value = 1 + vec[i-1][i];
                vec[i][j]=value;
            }
            else if(j<i)
            {
                vec[i][j]=0;
            }
            else
            {
                vec[i][j] = 1+((vec[i-1][j]+vec[i][j-1])/2);
            }
        }
    }
    /*for(i=0;i<=rr;i++)
    {
        for(j=0;j<=rr;j++)
            cout<<vec[i][j]<<" ";
        cout<<endl;
    }*/
    i=0;
    while(i<t)
    {
        rr= data[i].first;
        cc=data[i].second;
        value=vec[min(rr,cc)][max(rr,cc)];
        i++;
        cout << fixed;
        cout << setprecision(6);
        cout<<"Case #"<<i<<": "<<value<<endl;
    }
}
