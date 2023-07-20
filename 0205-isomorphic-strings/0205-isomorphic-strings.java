class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        
        if (s.length() != t.length())
            return false;
        
        Map<Character, Character> mp = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++){
            char original = s.charAt(i);
            char replacement = t.charAt(i);
            
            if (!mp.containsKey(original)){
                if (!mp.containsValue(replacement))
                    mp.put(original, replacement);
                else
                    return false;
            }
            else{
                if (replacement != mp.get(original))
                    return false;
            }
        }
        
        return true;
    }
}