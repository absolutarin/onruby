#include <stdio.h>

struct s {
	int i;
	char c;
}s;

int main()
{
	//printf ("%d\n",sizeof(*(&s)));
	//printf ("integer size:: %lu\n", sizeof(*(&s.i)));
	//char a=0;
	//short int b=0;
	//printf ("Sizeof a: %d\n", sizeof(a));
	//printf ("Sizeof b: %d\n", sizeof(b));
	//return sizeof(b)==sizeof(a+b);
	//int i = 16;
	//return (((((i >= i) << i) >> i) <= i));
	int i=0;
	return i++ + ++i;

}

