class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        int n = asteroids.length;
        Stack<Integer> st = new Stack();
        
       for (int i: asteroids) {
           
           while (!st.isEmpty() && i < 0 && st.peek() > 0) {
               int diff = i + st.peek();
               if (diff < 0)
                   st.pop();
               
               else if (diff > 0) 
                   i = 0;
               else {
                   i = 0;
                   st.pop();
               }
               
                   
           }
           if (i != 0)
               st.push(i);
           
       }
        
       int res[] = new int[st.size()];
        
       for (int i = st.size() - 1; i >= 0; i--) {
           res[i] = st.pop();
       }
        
        return res;
    }
}