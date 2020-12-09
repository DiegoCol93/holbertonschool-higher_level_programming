#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Insert a node on a ordered linked list.
 *
 *  Arguments:
 *    @head:   - Pointer to head of the list.
 *   @number:  - Number to add to new node.
 *
 *   Return:   - Pointer to newly created node or
 *               NULL if it fails.
 *
 * |------------ Written By Diego Lopez --------------|
 * |-------------- December - 8 - 2020 ---------------|
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *prev = NULL, *next = NULL;

	new = malloc(sizeof(listint_t)); /* Allocate new node. */
	if (!new)
		return (NULL);

	new->n = number; /* Set number for new node */

	if (head)
	{
		prev = *head; /* Set prev to start of list. */
		next = prev->next; /* Set next to the next node. */
		if (prev->n > number)
		{ /* If first number greater than new one*/
			new->next = prev; /* Set new->next to previous head. */
			*head = new; /* Set head to point to new node. */
			return (new);
		}
		while (next && next->n < number)
		{    /* Move through list. */
			prev = prev->next;
			next = next->next;
		}
		prev->next = new; /* Set the prev->next to the new node. */
		new->next = next; /* Set the new->next to the next node. */
	}
	return (new); /* Return the new node, or NULL if no head exist. */
}
