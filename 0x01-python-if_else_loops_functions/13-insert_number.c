#include "lists.h"
/**
 * insert_node - Inserts a nu a sorted singly-linked list.
 * @head: A pointer t of the linked list.
 * @number: The nu to insert.
 * Return: If function failed - NULL.
 * Or - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;

		new->next = node->next;
		node->next = new;
	}
	return (new);
}
