public class Stack<T> {
    private int max_size, top;
    private T[] array;
    public Stack(int max_size){
        this.max_size = max_size;
        @SuppressWarnings("unchecked")
        T[] array = (T[])new Object[max_size];
        this.array = array;
        this.top = -1;
    }

    public boolean empty() {
        return this.top == -1;
    }

    public boolean full() {
        return this.top == this.max_size - 1;
    }

    public void push(T x) throws StackOverflowException{
        if (this.full())
            throw new StackOverflowException();
        this.top ++;
        this.array[top] = x;
    }

    public T pop() throws StackIsEmpty{
        if (this.empty())
            throw new StackIsEmpty();
        this.top --;
        return this.array[top+1];
    }
}

class StackOverflowException extends Exception {}
class StackIsEmpty extends Exception  {}