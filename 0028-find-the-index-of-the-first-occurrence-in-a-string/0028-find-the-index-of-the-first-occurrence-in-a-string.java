class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.length() < needle.length()) {
            return -1;
        }
        
        int idx = 0;
        for (char c : haystack.toCharArray()) {
            if (c == needle.charAt(0) && haystack.length() - idx >= needle.length()) {
                if (haystack.substring(idx, idx+needle.length()).equals(needle)) {
                    return idx;
                }
            }

            idx += 1;
        }

        return -1;
    }
}