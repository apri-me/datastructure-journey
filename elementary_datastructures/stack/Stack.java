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

    public void push(T x) throws StackOverflowException{
        if (this.top == this.max_size - 1)
            throw new StackOverflowException();
        this.top ++;
        this.array[top] = x;
    }

    public T pop() throws StackIsEmpty{
        if (top == -1)
            throw new StackIsEmpty();
        this.top --;
        return this.array[top+1];
    }
}

class StackOverflowException extends Exception {}
class StackIsEmpty extends Exception  {}