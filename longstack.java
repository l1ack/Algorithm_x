import java.util.HashSet;
import java.util.Set;

public class longstack {
   public static int longestConsecutive(int[] nums){
    Set<Integer> num_set = new HashSet<Integer>();
    for(int num : nums){
        num_set.add(num);
    }
    int longstack;
    int currentnumber;
    int maxlongstack=0;
    System.out.println(555);
    for(int num : num_set){
        System.out.println(num);
        if(!num_set.contains(num-1)){//确定当前是最小的数;
            longstack=1;
            currentnumber=num;
            System.out.println(currentnumber);
            while(num_set.contains(currentnumber+1)){
            longstack+=1;
            currentnumber+=1;
        }
        maxlongstack=Math.max(longstack,maxlongstack);
    }

    //o(n) times;
    // traversal the array
    //hashset can reduce o(times) to 1;
}
return maxlongstack;

   } 
   public static void main(String[] args){
       int[] y= new int[]{1,2,4,6,3};
        int t=longstack.longestConsecutive(y);
        System.out.println(t);
}
}
