#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	unsigned int len = 0, half = 0, cmp = 0;
	listint_t *ptr1 = NULL;
	listint_t *ptr2 = NULL;

	if (!head || !*head)
		return (1);
	ptr1 = *head;
	ptr2 = *head;
	while (ptr2)
	{
		if (ptr2->next)
		{
			ptr2 = ptr2->next->next;
			len += 2;
		}
		else
		{
			ptr2 = ptr2->next;
			len++;
		}
	}
	len--;
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
