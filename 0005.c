#include <stdio.h>

int main(void)
{
    int divs[19] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    
    for (unsigned long long int i = 2520; 1; ++i)
    {
        for (int j = 0; j < 19; ++j)
        {
            if (!(i % divs[j] == 0))
            {
                goto end;
            }
        }
        printf("%llu\n", i);
        break;
        end:;
    }

    return 0;
}