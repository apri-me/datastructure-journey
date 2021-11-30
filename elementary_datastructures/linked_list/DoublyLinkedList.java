public class DoublyLinkedList<T> {
    /**
     * <p>
     * This is the implementation of doubly-linked-list in Java.
     * </p>
     * <p>
     * Hope you enjoy it
     * </p>
     */
    private Node<T> head;

    public void insert(Node<T> x) {
        if (this.head != null) {
            x.next = this.head;
            this.head.prev = x;
        }
        this.head = x;
    }

    public void insert(T v) {
        Node<T> x = new Node<>(v);
        this.insert(x);
    }

    public void delete(Node<T> x) {
        if (x.prev != null)
            x.prev.next = x.next;
        else
            this.head = x.next;
        if (x.next != null)
            x.next.prev = x.prev;
        x.next = null;
        x.prev = null;
    }

    public Node<T> search(T k) {
        Node<T> x = this.head;
        while (x != null) {
            if (x.data == k)
                return x;
            x = x.next;
        }
        return null;
    }

    public void print() {
        String s = "[";
        Node<T> x = this.head;
        while (x != null) {
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