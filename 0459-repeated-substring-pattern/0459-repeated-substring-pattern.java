class Solution {
    public boolean repeatedSubstringPattern(String s) {

        for (int i = 1; i <= s.length() / 2; i++) {
            String subString = s.substring(0, i);
            if (s.length() % subString.length() ==0) {
                if (s.equals(subString.repeat(s.length() / subString.length()))) {
                    return true;
                }
            }

        }
        return false;
    }
}