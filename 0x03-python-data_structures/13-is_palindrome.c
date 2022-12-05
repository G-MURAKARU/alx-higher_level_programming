#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	int counter = 0, default_size = 5, start = 0, end = 0;
	listint_t *current;
	listint_t **pointer_array = malloc(sizeof(listint_t *) * default_size);

	current = *head;

	while (current != NULL)
	{
		counter++;
		if (counter > default_size)
			pointer_array = realloc(pointer_array, (sizeof(listint_t *) * counter));
		pointer_array[counter - 1] = current;
		current = current->next;
	}

	end = --counter;

	while (start <= end)
	{
		if (pointer_array[start]->n != pointer_array[end]->n)
			return (0);
		start++;
		end--;
	}
	return (1);
}
