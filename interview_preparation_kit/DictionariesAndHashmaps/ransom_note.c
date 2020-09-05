#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <ctype.h>

char* readline();
char** split_string(char*);

struct Node {
    char *str;
    struct Node *next;
    int cnt;
};

struct Node *hashtable[30000] = {0};

unsigned int hash(char *str) {
    unsigned int h = 0;
    for(int i = 0; i < strlen(str); i++)
    {
        h *= 17;
        h += (str[i]-'A');
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
            if (!strcmp((probe)->str, str))
            {
                return probe;
            }
            probe = (probe)->next;
        }
        return NULL;
    }
}

void hashadd(char*str)
{
    struct Node* node = hashfind(str);
    struct Node** probe = NULL;

    if (node != NULL)
        node->cnt++;
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
        (*probe)->cnt = 1;
    }
}


bool hashdel(char*str)
{
    struct Node* probe = hashfind(str);

    if (probe != NULL)
        if (probe->cnt > 0)
        {
            probe->cnt--;
            return true;
        }
    return false;
}

// Complete the checkMagazine function below.
void checkMagazine(int magazine_count, char** magazine, int note_count, char** note) {
    struct Node * node = NULL;
    for (int i = 0; i < magazine_count; i++)
        hashadd(magazine[i]);
    
    for (int i = 0; i < note_count; i++)
    {
        if (!hashdel(note[i]))
        {
            printf("No\n");
            return;
        }
    }
    printf("Yes\n");
}

int main()
{
    char** mn = split_string(readline());

    char* m_endptr;
    char* m_str = mn[0];
    int m = strtol(m_str, &m_endptr, 10);

    if (m_endptr == m_str || *m_endptr != '\0') { exit(EXIT_FAILURE); }

    char* n_endptr;
    char* n_str = mn[1];
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    char** magazine_temp = split_string(readline());

    char** magazine = malloc(m * sizeof(char*));

    for (int i = 0; i < m; i++) {
        char* magazine_item = *(magazine_temp + i);

        *(magazine + i) = magazine_item;
    }

    int magazine_count = m;

    char** note_temp = split_string(readline());

    char** note = malloc(n * sizeof(char*));

    for (int i = 0; i < n; i++) {
        char* note_item = *(note_temp + i);

        *(note + i) = note_item;
    }

    int note_count = n;

    checkMagazine(magazine_count, magazine, note_count, note);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!line) {
            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);
    } else {
        data = realloc(data, data_length + 1);

        data[data_length] = '\0';
    }

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

