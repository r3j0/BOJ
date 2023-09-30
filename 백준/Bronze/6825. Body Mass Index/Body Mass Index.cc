#include <stdio.h>

int main(void) {
    double weight, height;
    scanf("%lf", &weight);
    scanf("%lf", &height);

    double bmi = weight / (height * height);
    if (bmi > 25) printf("Overweight");
    else if (bmi < 18.5) printf("Underweight");
    else printf("Normal weight");
    
    return 0;
}