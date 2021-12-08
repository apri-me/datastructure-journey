// Implementing doubly integer linked list with C++
#include <iostream>
using namespace std;

struct node // Defining structure of a single node
    {
    int val; // value of node
    node *next; // next node address
    node *prev; // previous node address
    };

class LinkedList{ // Defining a linked list 
    private:
        node *head, *tail; // Defining two node reference for head of linked list and tail of linked list
    public:
        LinkedList(); // Constructor of linked list
        void addNode(int n);// Adding new node to the tail
        node* search(int key);// Search a specific key in nodes of linked list
        void printer();// Print all available nodes with respect to their order
        void deleteNode(int key); // Delete a node with a specific key if this node exist.
};

LinkedList::LinkedList()
{
    head = NULL;
    tail = NULL;
}

void LinkedList::addNode(int n)
{
    node *tmp = new node();
    tmp->val = n;
    tmp->next = NULL;
    if (head == NULL)
    {
        tmp->prev = NULL;
        head = tmp;
        tail = tmp;
    }
    else
    {
        tmp->prev = tail;
        tail->next = tmp;
        tail = tail->next;
    }
}
node* LinkedList::search(int key)
{
    node *tmp;
    tmp = head;
    while (tmp != NULL && tmp->val != key)
    {
        tmp = tmp->next;
    }
    return tmp;
}

void LinkedList::printer()
{
    if(head == NULL)
    {
        cout << "NULL" << endl;
        return;
    }
    node *tmp;
    tmp = head;
    while (tmp != NULL)
    {
        cout << tmp->val << ' ';
        tmp = tmp->next;
    }
}

void LinkedList::deleteNode(int key)
{
    node *target = search(key);
    if (target == NULL)
    {
        return;
    }
    if (target == head)
    {
        head = target->next;
        target->next->prev = NULL;
    }
    else if (target == tail)
    {
        target->prev->next = NULL;
    }
    else
    {
        target->prev->next = target->next;
        target->next->prev = target->prev;
    }
}