public class Node{
    int data;
    Node next;
    public Node(int d){
        this.data = d;
        this.next = null;
    }

    public int getData(){
        return this.data;
    }

    public Node getNext(){
        return this.next;
    }

    public void setData(int newdata){
        this.data = newdata;
    }

    public void setNext(Node newnext){
        this.next = newnext;
    }    
}