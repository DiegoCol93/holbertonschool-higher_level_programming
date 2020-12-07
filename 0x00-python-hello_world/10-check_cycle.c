#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle.
 *
 *  Arguments:
 *    @list:   - Head pointer to the linked list.
 *
 *   Return:   - 0 If no cycle exists or 1 if one is found.
 *
 * |--------------- Written by Diego Lopez ---------------|
 * |----------------- December - 7 - 2020 ----------------|
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	if(!list || !list->next)
		return (0);
	while(hare && turtle)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if(turtle == hare || hare->next == turtle)
			return (1);
	}
	return (0);
}
