#include <stdio.h>

int main(void) {
    int f_a, f_o;
    int s_a, s_o;
    int m;
    scanf("%d %d",&f_a,&f_o);
    scanf("%d %d",&s_a,&s_o);
    // first : apple , second : orange
    m = s_a + f_o;
    // first : orange, second : apple
    if(m > f_a + s_o) {m = f_a + s_o;}
    
    printf("%d",m);
}