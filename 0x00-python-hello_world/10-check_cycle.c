#include "lists.h"

/**
 * check_cycle - a function that checks the linked list whether cycle or not
 * @list: linked list head pointer
 * Return: return 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	slow = fast = list;
	if (slow == NULL)
		return (0);
	while (slow != NULL)
	{
		if (fast->next == NULL || fast->next->next == NULL)
			return (0);
		if (fast->next == slow || fast->next->next == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
