class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hashmap1 = new HashMap<>();
        Map<Character, Integer> hashmap2 = new HashMap<>();


        for (char c : s.toCharArray()) {
            if (hashmap1.containsKey(c)) {
                hashmap1.put(c, hashmap1.get(c) + 1);
            }
            else {
                hashmap1.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (hashmap2.containsKey(c)) {
                hashmap2.put(c, hashmap2.get(c) + 1);
            }
            else {
                hashmap2.put(c, 1);
            }
        }
        
        if (hashmap2.equals(hashmap1)) {
            return true;
        }
        return false; 
    }
}