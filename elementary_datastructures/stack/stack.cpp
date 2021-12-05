// Implementation of stack data structure in C++
#include <bits/stdc++.h>
using namespace std;
//Size of stack:
#define SIZE 1000

template <typename T>

//Declare of stack class
class Stack{
    // top index holder.
    int top;
    public:
        T array[SIZE];
        Stack()
        {
            top = -1;
        }
        bool push(T x); //Append new number to stack.
        T pop(); // Pop last element of stack.
        T peek();// Return last element of stack.
        bool isEmpty(); // Check if stack is empty or not.
};

template <typename T>
bool Stack<T>::push(T x)
{
    if (top >= SIZE - 1)
    {
        cout << "ERROR! Stack overflow!" << endl;
        return false;
    }
    else
    {
        array[++top] = x;
        return true;
    }
}

template <typename T>
T Stack<T>::pop()
{
    if(top < 0)
    {
        cout << "ERROR! Stack underflow!" << endl;
        return (T)NULL;
    }
    else
    {
        T x = array[top--];
        return x;
    }
}

template <typename T>
T Stack<T>::peek()
{
    if (top < 0)
    {
        cout << "ERROR! Stack is empty!" << endl;
        return (T)NULL;
    }
    else
    {
        T x = array[top];
        return x;
    }
}

template <typename T>
bool Stack<T>::isEmpty()
{
    return (top<0);
}