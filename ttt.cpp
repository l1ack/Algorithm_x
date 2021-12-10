#include<stdio.h>
#include<ctype.h>
#include<iostream>
// #include<string>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        //以每一个字符串为基准，判断
        int num=0;
        int len=s.length();
        cout<<num<<'\n'<<endl;
        for(int i=0;i<len-1;i++){
            int j=1;
            while(s[i-j]==s[i+j] && j<i && j<len-1-i){
                j++;
                num++;
                cout<<num<<'\n'<<endl;
            }
            num++;
            j=1;
            while(s[i-j+1]==s[i+j] && j<i && j<len-1-i){
                j++;
                num++;
                cout<<num<<'\n'<<endl;
            }
            if(j>i || j>len-1-i)break;
        }
        return num;
    }
};
int main(){
    int i=0;
    char str[]="c3po2333 ###Test String.\n";
    string str1;
    getline(cin,str1);
    Solution er;
    i= er.countSubstrings(str1);
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
    printf("The first %d character are alpha.\n",i);
    return 0;
}
