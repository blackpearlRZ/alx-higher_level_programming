#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: int
* @next: next node ptr
*
* Description: singly linked list struct
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
