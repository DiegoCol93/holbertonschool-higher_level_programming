#include "lists.h"
#include <stdio.h>
unsigned int get_lenght(listint_t **head);
/**
 *
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 0, half = 0, cmp = 0;
	listint_t *ptr1 = NULL;
	listint_t *ptr2 = NULL;

	if (!head || !*head)
		return (1);
	ptr1 = *head;
	ptr2 = *head;
	len = get_lenght(head) - 1;
	if (len % 2 == 0)
		half = (len / 2);
	else
		half = (len / 2) + 1;
	for (; half > 0; half--)
	{
		ptr2 = *head;
		cmp = len;
		for (; cmp > 0; cmp--)
			ptr2 = ptr2->next;
		if (ptr1->n != ptr2->n)
			break;
		ptr1 = ptr1->next;
		len --;
	}
	if (half == 0 && cmp == 0)
		return (1);
	return (0);
}
unsigned int get_lenght(listint_t **head)
{
	listint_t *len = NULL;
	unsigned int nodes = 0;

	len = *head;
	while (len)
	{
		nodes++;
		len = len->next;
	}
	return (nodes);
}

