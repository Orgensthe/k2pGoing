#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

struct Node {
	char *str;
	int number;
	struct Node *next;
};

struct Node *hashtable[30000] = {0};

unsigned int hash(char *str) {
	unsigned int h = 0;
	for(int i = 0; i < strlen(str); i++)
	{
		h *= 17;
		h += (str[i]-'a');
	}
	return h % 30000;
}

struct Node* hashfind(char *str)
{
	unsigned int hashnum = hash(str);
	struct Node *probe = hashtable[hashnum];

	if (probe == NULL)
		return NULL;
	else
	{
		while(probe != NULL)
		{
			if(!strcmp(probe->str, str))
			{
				return probe;
			}
			probe = (probe)->next;
		}
		return NULL;
	}
}

void hashadd(char*str, int number)
{
	struct Node* node = hashfind(str);
	struct Node** probe = NULL;

	if (node != NULL)
		node->number = number;
	else 
	{
		probe = &hashtable[hash(str)];
		if ((*probe) != NULL) {
			while((*probe)->next != NULL)
				probe = &(*probe)->next;
			(*probe)->next = (struct Node*)malloc(sizeof(struct Node));
			probe = &(*probe)->next;
		} else {
			(*probe) = (struct Node*)malloc(sizeof(struct Node));
		}
		(*probe)->str = (char*)malloc(strlen(str));
		strcpy((*probe)->str, str);
		(*probe)->next = NULL;
		(*probe)->number = number;
	}
}

int main() {

	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	FILE* fp;
	int querycnt, number;
	char namebuffer[256];
	struct Node *probe;

	fp = fopen("./input02.txt", "r");

	fscanf(fp, "%d\n", &querycnt);

	for(int i = 0; i < querycnt; i++)
	{
		fscanf(fp, "%s %d\n", namebuffer, &number);
		hashadd(namebuffer, number);
	}

	number = 0;
	while (fscanf(fp, "%s\n", namebuffer) > 0)
	{
		if(number) {
			printf("\n");
		}
		probe = hashfind(namebuffer);
		if (probe)
			printf("%s=%d", probe->str, probe->number);
		else {
			printf("Not found");
		}
		number = 1;
	}
	return 0;
}

