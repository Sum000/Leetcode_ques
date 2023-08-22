class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        
        backtrack("(", 1, 0, res, n);
        return res;
    }
    
    static void backtrack(String curr, int op, int cl, List<String> res, int n) {
        
        if (curr.length() == 2*n) {
                 res.add(curr);
              return;
        }
        
        if (op < n) backtrack(curr + "(", op + 1, cl, res, n);
        if (cl < op) backtrack(curr + ")", op, cl + 1, res, n);
    }
}