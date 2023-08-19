class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        
        if (m > n)
            return false;
        
        int s1map[] = new int[26];
        int s2map[] = new int[26];
        
        for (int i = 0; i < m; i++) {
            s1map[s1.charAt(i) - 'a']++;
            s2map[s2.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < n - m; i++) {
            if (matches(s1map, s2map))
                return true;
            
            s2map[s2.charAt(i + m) - 'a']++;
            s2map[s2.charAt(i) - 'a']--;
        }
        return matches(s1map, s2map);
    }
    
    static boolean matches(int s1map[], int s2map[]) {
        for (int i = 0; i < 26; i++) {
            if (s1map[i] != s2map[i])
                return false;
        }
        return true;
    }
}