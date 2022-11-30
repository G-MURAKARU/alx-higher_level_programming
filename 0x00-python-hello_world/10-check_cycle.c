#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: pointer to linked list head node
 *
 * Return: 1 if present, 0 if absent
 */
int check_cycle(listint_t *list)
{
	int n = 2;
	int counter;
	int array_counter = 0;
	int temp_counter;
	listint_t **temp;
	listint_t *current;
	listint_t **array_pointers;

	array_pointers = malloc(sizeof(listint_t *) * n);
	if (!array_pointers)
		return (-1);

	current = list;
	while (current)
	{
		for (counter = 0; counter < n && (array_pointers[counter] != NULL);
				counter++)
		{
			if (current == array_pointers[counter])
				return (1);
		}
		array_counter++;
		if (array_counter != n)
		{
			array_pointers[counter] = current;
			current = current->next;
			continue;
		}
		temp = array_pointers;
		array_pointers = malloc(sizeof(listint_t *) * ++n);
		for (temp_counter = 0; temp_counter < array_counter; temp_counter++)
			array_pointers[temp_counter] = temp[temp_counter];
		free(temp);
		current = current->next;
	}
	return (0);
}

