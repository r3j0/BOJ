#include <stdio.h>

int main(void)
{
	int n;
	int sc[1000];
	int max = 0;
	double result =0;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&sc[i]);
	}
	for(int i=0;i<n;i++)
	{
		if(max < sc[i])
			max = sc[i];
	}
	for(int i=0;i<n;i++)
	{
		result += ((double)sc[i]/max)*100;
	}
	printf("%f",result/n);
    return 0;
}