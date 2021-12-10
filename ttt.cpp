#include<stdio.h>
#include<ctype.h>
#include<iostream>
// #include<string>
using namespace std;

    string s;
class Solution {
public:
    int countSubstrings() {
        cin>>s;
        //以每一个字符串为基准，判断
        int num=0;
        int len=s.length();
        for(int i=0;i<len;i++){
            int j=1;
            while(s[i-j]==s[i+j] && j<=i && j<=len-1-i){
                j++;
                num++;
            }
            num++;
            j=1;
            while(s[i-j+1]==s[i+j] && j<=i && j<=len-1-i){
                j++;
                num++;
                cout<<num<<'\n'<<endl;
            }
        }
        return num;
    }
};
int main(){
    int i=0;
    char str[]="c3po2333 ###Test String.\n";

    Solution er;
    i= er.countSubstrings();
    // isalpha() 或者 isdigit() 检测后返回“真”，那么它被 isalnum() 检测后也一定会返回“真”
    // while(str1[i]){
    //     putchar(tolower(str1[i]));
    //     i++;
    // }
    // i=0;
    // while(isalnum(str1[i])){
    //     //if(isalpha(str[i]))
    //     i++;
    // }
    printf("The largest %d character are symmetry.\n",i);
    return 0;
}
