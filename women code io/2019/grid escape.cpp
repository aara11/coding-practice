#include<bits/stdc++.h> 
using namespace std; 
  
int main() 
{
    long long t,i=0,k,r,c,j;
    cin>>t;
    while(i<t)
    {
        cin>>r>>c>>k;
        int num = (r*c)-k;
        if(num<=1)
        {    cout<<"Case#"+str(i)+": IMPOSSIBLE"<<endl;
            continue;
        }
        if (c==1)
        {
            cout<<"Case#"+str(i)+": POSSIBLE"<<endl;
            cout<<"S"<<endl;num--;r--;
            for(i=1;i<r;i++)
            {
                if(num>0)
                {
                    num--;cout<<"N"<<endl;
                }
                else
                cout<<"S";
            }
        }
        else
        {
            cout<<"Case#"+str(i)+": POSSIBLE"<<endl;
            cout<<"E";num--;
            for(i=1;i<c;i++)
            {
                if(num>0)
                {
                    cout<<"W";num--;
                }
                else
                cout<<"S";
            }
            for(i=1;i<r;i++)
            {
                for(j=0;j<c;j++)
                {
                    if(num>0)
                    {    cout<<"N";num--;}
                    else
                    cout<<"S";
                }
                cout<<endl;
            }
            
        }      
        
        i++;
    }
}