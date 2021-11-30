public class CyclicDoublyLinkedList<T> {
    /**
     * <p>
     * This is the implementation of cyclic-doubly-linked-list in Java.
     * </p>
     * <p>
     * Hope you enjoy it
     * </p>
     */
    private Node<T> sentinel;

    public CyclicDoublyLinkedList() {
        sentinel = new Node<T>(null);
        sentinel.next = sentinel;
        sentinel.prev = sentinel;
    }

    public void insert(Node<T> x) {
        x.next = this.sentinel;
        x.prev = this.sentinel.prev;
        this.sentinel.prev.next = x;
        this.sentinel.prev = x;
    }

    public void insert(T v) {
        Node<T> x = new Node<>(v);
        this.insert(x);
    }

    public void delete(Node<T> x) throws SentinelNotDeletableException {
        if (this.sentinel.equals(x))
            throw new SentinelNotDeletableException();
        x.prev.next = x.next;
        x.next.prev = x.prev;
    }

    public Node<T> search(T k) {
        Node<T> x = this.sentinel.next;
        while (x != null && !x.equals(sentinel)) {
            if (x.data == k)
                return x;
            x = x.next;
        }
        return null;
    }

    public void print() {
        String s = "[";
        Node<T> x = this.sentinel.next;
        while (x != null && !x.equals(sentinel)) {
            s += x.data.toString();
            s += ", ";
            x = x.next;
        }
        s += "]";
        System.out.println(s);
    }
    
}

class Node<T> {
    T data;
    Node<T> next;
    Node<T> prev;

    Node(T data) {
        this.data = data;
    }
}

class SentinelNotDeletableException extends Exception {}