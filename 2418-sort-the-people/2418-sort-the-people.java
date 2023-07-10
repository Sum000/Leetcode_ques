class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        String[] res = new String[heights.length];
        
        HashMap<Integer, String> mp = new HashMap<>();
        
        for (int i = 0; i < heights.length; i++){
            mp.put(heights[i], names[i]);
        }
        
        Arrays.sort(heights);
        
        int index = 0;
        
        for (int i = heights.length - 1; i >= 0; i--){
            res[index] = mp.get(heights[i]);
            index++;
        }
        
        return res;
    }
}