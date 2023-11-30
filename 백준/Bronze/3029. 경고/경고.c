#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main(void){
    int hour,min,sec;
    int hour2,min2,sec2;
    scanf("%d:%d:%d",&hour,&min,&sec);
    scanf("%d:%d:%d",&hour2,&min2,&sec2);
    int start_sec = hour * 3600 + min * 60 + sec;
    int end_sec = hour2 * 3600 + min2 * 60 + sec2;
    int wait_time = end_sec - start_sec;
    if (wait_time <=0) {
        wait_time += 86400;
    }
    int wait_hour = wait_time / 3600;
    int wait_min = (wait_time % 3600) / 60;
    int wait_sec = wait_time % 60;
    printf("%02d:%02d:%02d",wait_hour,wait_min,wait_sec);
    
  return 0;

}