#include<stdio.h>
#include<stdlib.h>
char input[1000005];
int word_count(char* str){
    int count=0, i=0;
    while (1){
        if(str[i]=='\0'){
            break;
        }
        else if((str[i]!=32)&&((str[i+1]==32)||(str[i+1]=='\0'))){
            count++;
        }
        i++;
    }
    return count;
}
int main(){
    
    int word;
    gets(input);
    word=word_count(input);
    printf("%d\n", word);
    return 0;
}