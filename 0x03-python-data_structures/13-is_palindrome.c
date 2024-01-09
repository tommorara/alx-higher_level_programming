#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome-function in C that checks if a singly linked list
 * is a palindrome
 * @head: pointer to the pointer to the head of the list
 * Return: 0 if it's not a palindrome else return 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *_ptr;
	int arr[4000] = {0};
	int length = 0, q_index = 4000 - 1;

	if (head == NULL)
		return (1);
	_ptr = *head;
	if (_ptr == NULL || _ptr->next == NULL)
		return (1);
	while (_ptr != NULL)
	{
		arr[q_index] = _ptr->n;
		length++;
		q_index--;
		_ptr = _ptr->next;
	}
	_ptr = *head;
	q_index++;
	while (_ptr != NULL)
	{
		if (_ptr->n != arr[q_index])
			return (0);
		q_index++;
		_ptr = _ptr->next;
	}
	return (1);
}
