#include "lists.h"

/**
 * sum_dlistint - sum of all the data
 *
 * @head: pointer head list
 *
 * Return: return the sum of all the data or 0 if it is empty
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *tmp;
	int sum = 0;

	tmp = head;

	if (tmp == NULL)
		return (0);
	while (tmp != NULL)
	{
		sum = sum + tmp->n;
		tmp = tmp->next;
	}
	return (sum);
}
