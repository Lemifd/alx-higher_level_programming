#include "lists.h"

/**
 * get_dnodeint_at_index - get the nth node of a linked list
 *
 * @head: pointer head of the list
 * @index: position
 *
 * Return: return the node or NULL if it not exist
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *tmp;
	unsigned int num_nodes = 0;

	tmp = head;
	while (tmp != NULL && num_nodes <= index)
	{
		if (num_nodes == index)
			return (tmp);
		tmp = tmp->next;
		num_nodes++;
	}
	return (NULL);
}
