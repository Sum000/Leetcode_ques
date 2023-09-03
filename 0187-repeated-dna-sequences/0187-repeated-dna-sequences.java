class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int len = s.length();
        if (len > 10000)
            return new ArrayList<>();
        
        HashSet<String> repeatedSeqSet = new HashSet<>();
        HashSet<String> resultSeq = new HashSet<>();

        for (int i = 0 ; i < len-9 ; i++){
            String windowString = s.substring(i, i+10);

            if (!repeatedSeqSet.contains(windowString))
                repeatedSeqSet.add(windowString);
            else
                resultSeq.add(windowString);
        }

        return new ArrayList<>(resultSeq);
    }
}