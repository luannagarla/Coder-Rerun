#include <stdio.h>

int copo[3] = {0, 0, 0};

void m1(){
    int aux = copo[1];
    copo[1] = copo[0];
    copo[0] = aux; 
}

void m2(){
    int aux = copo[2];
    copo[2] = copo[1];
    copo[1] = aux;
}
void m3(){
    int aux = copo[2];
    copo[2] = copo[0];
    copo[0] = aux; 
}

int main(){
    int n;
    char L;
    
    scanf("%d", &n); //quantos movimentos vão ter
    scanf("\n %c", &L); //leitura da moeda
    
    if (L == 'A') { // onde começa a moeda
        copo[0] = 1;
    } else if(L == 'B') {
        copo[1] = 1;
    } else if(L == 'C'){
        copo[2] = 1;
    }
    
    int aux;
    int i;
    for(i = 1; i <= n; i++){
        scanf("%d", &aux);
        if (aux == 1) {
            m1();
        } else if(aux == 2) {
            m2();
        } else {
            m3();
        }
    }

    if (copo[0] == 1) {
        printf("A");
    } else if(copo[1] == 1) {
        printf("B");
    } else {
        printf("C");
    }
    
    return 0;
} 