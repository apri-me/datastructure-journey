public class LinkedList<T> {
    /**
     * <p>
     * This is the implementation of linked-list in Java.
     * </p>
     * <p>
     * Hope you enjoy it
     * </p>
     */
    private Node<T> head;

    public void insert(Node<T> x) {
        x.next = this.head;
        this.head = x;
    }

    public void insert(T v) {
        Node<T> x = new Node<>(v);
        this.insert(x);
    }

    public void delete(Node<T> previous_node) throws NullElementException {
        Node<T> x;
        if (previous_node != null) {
            x = previous_node.next;
            if (x == null)
                throw new NullElementException();
            previous_node.next = x.next;
            x.next = null;
        } else {
            if (this.head == null)
                throw new NullElementException();
            x = this.head.next;
            this.head.next = null;
            this.head = x;
        }
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

    Node(T data) {
        this.data = data;
    }
}

class NullElementException extends Exception {
}