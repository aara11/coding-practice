#include<bits/stdc++.h>
//FILE* f1 = freopen("input1.txt","r",stdin);
//FILE* f2= freopen("output1.txt","w",stdout);
using namespace std;

long long get_ct(string s){
    int ans=0;
    vector<bool> vec(26,false);
    for(int i=0;i<s.size();i++){
        if(s[i]==' ')
        continue;
        vec[s[i]-'A']=true;
    }
    for(int i=0;i<26;i++)
        if(vec[i])
            ans+=1;
    return ans;
}


int main()
{
    long long t;
    cin>>t;
    for(long long tt=1;tt<=t;tt++)
    {
        long long n;
        cin>>n;
        string ans="";
        string temp;
        getline(cin,temp);
        long long count=0,ct;
        for(int i=0;i<n;i++){
            getline(cin,temp);
            ct=get_ct(temp);
            if(count<ct){
                count=ct;
                ans=temp;
            }
            else if(ct==count){
                if(temp<ans)
                    ans=temp;
            }
        }
        cout<<"Case #"<<tt<<": ";
        cout<<ans;
        cout<<endl;
    }
}