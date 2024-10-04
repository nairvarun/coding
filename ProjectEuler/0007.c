#include <stdio.h>

int is_prime(unsigned long long int n)
{
    for (int i = 2; i < n/2; ++i)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    unsigned long long int i = 0, n = 1;
    while (i < 10001)
    {
        if (is_prime(n))
        {
            ++i;
        }
        ++n;
    }
    printf("%llu\n", n - 1);
    return 0;
}