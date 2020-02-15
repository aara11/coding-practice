#include<bits/stdc++.h>

using namespace std;
bool sortbysec(const pair<long long, long long> &a, const pair<long long, long long> &b)
{
    return (a.second < b.second);
}


int main()
{
    long long num,t,i=0, level, n,j,a,b;
    cin>>t;
    while(i<t)
    {
        vector<pair<long long, long long> > vec;
        cin>>n;
        for(j=0;j<n;j++)
        {
            cin>>a>>b;
            vec.push_back(make_pair(a,b));
        }
        sort(vec.begin(), vec.end(), sortbysec);
        num=0;
        long long val,max_=0;
        for(j=0;j<n;j++)
        {
            val=min(num, vec[j].first * vec[j].second);
            num=num+vec[j].first-val;
            max_=vec[j].second;
        }
        level=max(num,max_+1);
        //level=max(1,level);
        i++;
        cout<<"Case #"<<i<<": "<<level<<endl;
    }
}
