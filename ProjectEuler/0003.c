#include <stdio.h>
#include <math.h>

int check_prime(long long int num)
{
    long long int r = sqrt(num);
    for (long long int i = 2; i < r; ++i)
    {
        if (num % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

void max_pfac(long long int num)
{
    long long int r = sqrt(num);
    for (long long int i = r; i > 0; --i)
    {
        if (num % i == 0)
        {
            if (check_prime(i))
            {
                printf("%lld\n", i);
                break;
            }
        }
    }
    
}

int main(void)
{
    long long int num = 600851475143;
    max_pfac(num);

    return 0;
}