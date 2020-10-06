#include <stdio.h>

int main(){
    float a; 
    float b; 
    float c;
    float d;
    scanf("%f %f %f %f", &a, &b, &c, &d);
    if (a+b+c+d != 0){
        printf("%0.5f", ((a/2) + b) * c / d);
    }
return 0;
}  