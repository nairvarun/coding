#include <stdio.h>
#include <math.h>

int check_500pfac(int x) {
    int numpfactors = 0;
    for (double i = 1; i <= sqrt(x); ++i) {
        if ((int)x % (int)i == 0) {
            numpfactors += 2;
        }
    }
    if (numpfactors > 500) {
        printf("%d\n", x);
        return 1;
    } else {
        return 0;
    }
}

int main(void) {
    int trinum;
    for (int i = 1; 1; ++i) {
        trinum = 0;
        for (int j = 1; j <= i; ++j) {
            trinum += j;
        }
        if (check_500pfac(trinum)) {
            break;
        }
    }
    return 0;
}
