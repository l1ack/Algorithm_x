import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.Queue;

public class DequeTest {
    public static void main(String[] args){
        Deque<Integer> mDeque= new ArrayDeque<>();
        Queue<Integer> queue= new PriorityQueue<>();
        //Deque<Integer> m1Deque= new LinkedList<>();
        //首先我们看Deque的实现类ArrayQueue的数据结构，可以看到ArrayQueue还是使用数组的结构，应该来说数组是实现集合类的基础数据结构
        //双端队列作为Queue和Stack的双重实现，但是在使用的时候只能选择一种使用，不能Queue与Stack的api同时使用
        //Deque双端队列介绍:Deque是Queue子接口，是双端队列。可以同时从两端（队列头部和尾部）添加、删除元素。所以可以用来实现栈的数据结构。有两个实现类（ArrayDeque和LinkedList）

        for (int i = 0;i <5 ;i++){
            mDeque.offer(i);
        }
        System.out.println(mDeque.peek());
        System.out.println("******************集合方式遍历******************");
        for(Integer x : mDeque){
            System.out.println(x);
        }
        System.out.println("******************遍历队列**********************");
        //队列方式遍历，元素逐个被移除；
        while(mDeque.peek()!=null){
            System.out.println(mDeque.poll());
        }
        System.out.println("*****************进栈操作********************");
        mDeque.push(10);
        mDeque.push(15);
        mDeque.push(24);
        print(mDeque);
        //出栈操作
        System.out.println("******************出栈操作********************");
        System.out.println(mDeque.pop());
    }
    public static void print(Deque<Integer> queue){
        for (Integer x:queue){
            System.out.println(x);
        }
    }
}
