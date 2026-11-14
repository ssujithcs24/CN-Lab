#include <stdio.h>
int min(int x, int y)
{
    if (x < y)
        return x;
    else
        return y;
}
int main()
{
    int drop = 0, mini, nsec, cap, count = 0, i, inp[25], process;
    printf("Enter the bucket size:\n");
    scanf("%d", &cap);
    printf("Enter the processing rate:\n");
    scanf("%d", &process);
    printf("Enter the number of seconds you want to simulate:\n");
    scanf("%d", &nsec);
    for (i = 0; i < nsec; i++)
    {
        printf("Enter the size of the packet entering at %d sec:\n", i + 1);
        scanf("%d", &inp[i]);
    }
    printf("\nSecond | Packet Received | Packet Sent | Packet Left | Dropped\n");
    printf("--------------------------------------------------------------\n");
    for (i = 0; i < nsec; i++)
    {
        count += inp[i];
        if (count > cap)
        {
            drop = count - cap;
            count = cap;
        }
        printf("%d\t %d\t\t", i + 1, inp[i]);
        mini = min(count, process);
            printf("%d\t\t", mini);
        count = count - mini;
        printf("%d\t\t %d\n", count, drop);
        drop = 0;
    }
    for (; count != 0; i++)
    {
        if (count > cap)
        {
            drop = count - cap;
            count = cap;
        }
        printf("%d\t 0\t\t", i + 1);
        mini = min(count, process);
        printf("%d\t\t", mini);
        count = count - mini;
        printf("%d\t\t %d\n", count, drop);
        drop = 0;
    }
    return 0;
}