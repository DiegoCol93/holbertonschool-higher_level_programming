#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int get_lenght_recursive(listint_t *copy, int n);
int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = NULL, *ptr2 = NULL;
	unsigned int len = 0, half = 0, cmp = 0;

	if (!head || !*head)
		return (1);
	ptr1 = *head;
	ptr2 = *head;
	len = get_lenght_recursive(ptr2, 0);
	if (len % 2 == 0)
		half = (len / 2);
	else
		half = (len / 2) + 1;
	for (; half > 0; half--)
	{
		ptr2 = ptr1;
		cmp = len;
		for (; cmp > 0; cmp--)
			ptr2 = ptr2->next;
		if (ptr1->n != ptr2->n)
			break;
		ptr1 = ptr1->next;
		len -= 2;
	}
	if (half == 0 && cmp == 0)
		return (1);
	return (0);
}
int get_lenght_recursive(listint_t *copy, int n)
{
        if(!copy->next)
		return (n);
	else
		return (n);
        copy = copy->next;
        get_lenght_recursive(copy, n);
}
