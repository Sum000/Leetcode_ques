class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length();
        int charCount[] = new int[26];
        int start = 0;
        int maxCount = 0;
        int end = 0;
        int maxLength = 0;
        
        for (end = 0; end < n; end++) {
            charCount[s.charAt(end) - 'A']++;
            
            int currCharCount = charCount[s.charAt(end) - 'A'];
            
            maxCount = Math.max(maxCount, currCharCount);
            
            while ((end - start + 1 - maxCount) > k) {
                charCount[s.charAt(start) - 'A']--;
                start++;
            }
            
            maxLength = Math.max(maxLength, end - start + 1);
        }
        
        return maxLength;
    }
}