#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

int main () 
{
	char data[400] = "s";
	FILE *fdin;
	FILE *fdout;
	FILE *data_out;
	fdin = fopen("/dev/ttyAMA0", "w");
	fdout = fopen("/dev/ttyAMA0", "r");
	data_out = fopen("data.txt", "r+");

	if (fdin == NULL || fdout == NULL || data_out == NULL) {
		printf("Error opening file(s)\n");
		return -1;
	}
	fprintf(fdin, "s\n");
	sleep(5);
	printf("Trying to grab data\n");
	fgets(data, 400, fdout);
	printf("Data grabbed\n");
	fprintf(data_out, "%s", data);

	//while(1) {i
	//	fgets(data, 200, fd);
	  //     	printf("%s", data);	
	//	}
	fclose(fdin);
	fclose(fdout);
	fclose(data_out);
	return 0;
}

