public class Queue<T> {
    private int head, tail, max_size, length = 0;
    private T[] array;

    public Queue(int max_size){
        if (max_size < 0)
            throw new NegativeArraySizeException();
        this.max_size = max_size;
        @SuppressWarnings("unchecked")
        T[] array = (T[])new Object[max_size];
        this.array = array;
        this.head = 0;
        this.tail = -1;
    }

    public void enqueue(T x) throws QueueOverflowException{
        if (this.length >= max_size)
            throw new QueueOverflowException();
        this.tail ++;
        this.tail %= max_size;
        this.array[tail] = x;
        this.length ++;
    }

    public T dequeue() throws QueueIsEmptyException{
        if (this.length == 0)
            throw new QueueIsEmptyException();
        T x = this.array[head];
        this.head ++;
        this.head %= max_size;
        this.length --;
        return x;
    }
}

class QueueOverflowException extends Exception {}
class QueueIsEmptyException extends Exception {};