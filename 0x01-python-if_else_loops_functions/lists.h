#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - singly ld list
 * @b: integer
 * @next: points to the ne
 * Description: siked list node structure
 *
 */
typedef struct listint_s
{
	int b;
	struct listint_s *nexto;
} listint_t;
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int b);
void free_listint(listint_t *head);
listint_t *insert_node(listint_t **head, int number);
#endif /* LISTS_H */
