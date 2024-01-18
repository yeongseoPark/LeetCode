class Solution {
    public String mergeAlternately(String word1, String word2) {
        int one = 0;
        int two = 0;

        StringBuilder sb = new StringBuilder();

        while (one < word1.length() && two < word2.length()) {
            sb.append(word1.charAt(one));
            sb.append(word2.charAt(two));

            one += 1;
            two += 1;
        }

        if (one < word1.length()) {
            sb.append(word1.substring(one));
        }
        else {
            sb.append(word2.substring(two));
        }

        return sb.toString();
    }
}

