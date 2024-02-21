#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	unsigned char buf[1];
	read(0, buf, 2048);
	printf("%c\n", buf[0]);
	return 0;
}

void victory() {
	printf("You win!");
}
