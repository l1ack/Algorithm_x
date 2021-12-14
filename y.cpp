#include<algorithm>
#include<iostream>
#include<cstdio>
using namespace std;
const int MAXN=1e5+3;
struct emm{
    int a,b;
}ss[MAXN],sa[MAXN],sb[MAXN];
bool cmpa(emm qaq,emm qwq){
    return qaq.a<qwq.a;
}
bool cmpb(emm qaq,emm qwq){
    return qaq.b<qwq.b;
}
int topa,topb;
int n;
int binsrchb(int l,int r,int x);
void searchb(int x);
int binsrcha(int l,int r,int x){//宸﹂棴鍙冲紑
    // printf("binsrcha %d %d %d\n",l,r,x);
    if(l==r-1)return l;
    int mid=(l+r)>>1;
    if(sa[mid].a>x)return binsrcha(l,mid,x);
    else return binsrcha(mid,r,x);
}
void searcha(int x){
    // printf("searcha %d\n",x);
    if(x>=sa[topa].a)return;
    int c=binsrcha(1,topa+1,x);
    // printf("c= %d\n",c);
    for(--topa;topa>=c;--topa)searchb(sa[topa].b);
    topa++;
    return;
}
int binsrchb(int l,int r,int x){//宸﹂棴鍙冲紑
    // printf("binsrchb %d %d %d\n",l,r,x);
    if(l==r-1)return l;
    int mid=(l+r)>>1;
    if(sb[mid].b>x)return binsrchb(l,mid,x);
    else return binsrchb(mid,r,x);
}
void searchb(int x){
    // printf("searchb %d\n",x);
    if(x>=sb[topb].b)return;
    int c=binsrchb(1,topb+1,x);
    // printf("c= %d\n",c);
    for(--topb;topb>=c;--topb)searcha(sb[topb].a);
    topb++;
    return;
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        sa[0].a=sa[0].b=sb[0].a=sb[0].b=-1e9-7;
        sa[n+1].a=sa[n+1].b=sb[n+1].a=sb[n+1].b=1e9+7;
        for(int i=1;i<=n;++i){
            scanf("%d",&sa[i].a);
            ss[i].a=sb[i].a=sa[i].a;
        }
        for(int i=1;i<=n;++i){
            scanf("%d",&sa[i].b);
            ss[i].b=sb[i].b=sa[i].b;
        }
        sort(sa+1,sa+n+1,cmpa);
        sort(sb+1,sb+n+1,cmpb);
        topa=topb=n+1;
        searcha(sb[n].a);
        searchb(sa[n].b);
        // printf("topa = %d ; topb = %d\n",topa,topb);
        for(int i=1;i<=n;++i){
            if(ss[i].a>=sa[topa].a||ss[i].b>=sb[topb].b){
                printf("1");
            }
            else printf("0");
        }
        printf("\n");
    }
    return 0;
}