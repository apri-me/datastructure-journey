//Implementing of Queue data structure in C++.
#include <bits/stdc++.h>
using namespace std;

// Define default size for queue.
#define SIZE 1000
template <typename T>
class Queue
{
    T *array; // array of queue.
    int capacity;// capacity of queue.
    int front;// front element index of queue.
    int rear;// rear element index of queue.
    int count;// count of reserved elemenets in queue.

    public:
        Queue(int size);// Constructor
        ~Queue();// Deconstructor

        T dequeue(); // dequeue front element of queue.
        void enqueue(T x); // enqueue new element in queue's rear
        T peek();// return front element of queue.
        int size();// return size of queue.
        bool isEmpty();// return if queue is empty.
        bool isFull();// return if queue is full.
};

template <typename T>
Queue<T>::Queue(int size)
{
    array = new T[size];
    capacity = size;
    front = 0;
    rear = -1;
    count = 0;
}

template <typename T>
Queue<T>::~Queue()
{
    delete[] array;
}

template <typename T>
T Queue<T>::dequeue()
{
    if (isEmpty())
    {
        cout << "ERROR! Underflow!";
        exit(EXIT_FAILURE);
    }
    T x = array[front];
    front = (front + 1 ) % capacity;
    count--;
    return x;
}

template <typename T>
void Queue<T>::enqueue(T x)
{
    if (isFull())
    {
        cout << "ERROR! Overflow!";
        exit(EXIT_FAILURE);
    }

    rear = (rear + 1) % capacity;
    array[rear] = x;
    count++;
}

template <typename T>
T Queue<T>::peek()
{
    if (isEmpty())
    {
        cout << "ERROR! Underflow!";
        exit(EXIT_FAILURE);
    }
    return array[front];
}

template <typename T>
int Queue<T>::size()
{
    return count;
}

template <typename T>
bool Queue<T>::isEmpty()
{
    return (size() == 0);
}

template <typename T>
bool Queue<T>::isFull()
{
    return (size() == capacity);
}
