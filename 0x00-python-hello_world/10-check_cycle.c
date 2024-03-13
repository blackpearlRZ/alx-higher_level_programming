#include "lists.h"

/**
* check_cycle - ccheks linked list cycle
* @list: head ptr
* Return: 0 if cycle exits , 1 if it doesn't
*/
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

if (list == NULL)
return (0);

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}

return (0);
}
