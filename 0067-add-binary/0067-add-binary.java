class Solution {
    public String addBinary(String a, String b) {
        
        int n1 = a.length();
        int n2 = b.length();
        
        int carry = 0, sum;
        
        int i = n1 - 1;
        int j = n2 - 1;
        
        StringBuilder str = new StringBuilder();
        
        while (i >= 0 || j >= 0 || carry > 0){
            
            sum = carry;
            
            if (i >=0)
                sum += a.charAt(i--) - '0';
            
            if (j >= 0)
                sum += b.charAt(j--) - '0';
            
            str.insert(0, sum % 2);
            carry = sum / 2;
        }
        
        return str.toString();
    }
}