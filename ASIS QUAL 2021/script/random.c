#include <stdio.h>
#include <stdlib.h>
 
int main(void)
{
    srand(0xf5f38a17);
    for(int i = 0; i < 32; i++)
        printf("%d, ", rand());
    return 0;
}