#include <stddef.h>

size_t print_listint(const listint_t *h)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}

