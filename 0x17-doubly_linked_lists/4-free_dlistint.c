#include "lists.h"

/**
 * free_dlistint - free a list
 *
 * @head: pointer head of list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;

	while (head != NULL)
	{
		tmp = head;
		head = head->next;
		free(tmp);
	}
}
