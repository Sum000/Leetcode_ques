class Solution {
    public int countSegments(String s) {
                int count = 0;
        int n = s.length();
        
        if (s.isEmpty())
            return 0;
        
        int p = 0, r = n - 1;
        while (p < n && s.charAt(p) == ' '){
            p++;
        }
        
        if (p == n)
            return 0;
        
        while (r >= 0 && s.charAt(r) == ' ')
            r--;
        
        if (r < p)
            return 0;
        
        for (int i = p; i <= r; i++) {
            if (s.charAt(i) == ' ' && (i == p || s.charAt(i - 1) != ' '))
                count++;
        }
        return count + 1;
    }
}