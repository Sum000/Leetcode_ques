class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
      
        
        Set<String> seen = new HashSet<>();
        Set<String> res = new HashSet<>();
        
        int len = s.length();
        
        for (int i = 0; i < len - 9; i++) {
            String cur = s.substring(i, i + 10);
            
            if (seen.contains(cur))
                res.add(cur);
           
            seen.add(cur);
        }
          List<String> li = new ArrayList<>(res);
        
        return li;
    }
}