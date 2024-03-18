class Solution {
    public int arraySign(int[] nums) {
        int res = 0;

        for (int i : nums) {
            if (i == 0) return 0;
            
            if (i > 0 && res == 0) {
                res = 1;
            } else if (i < 0 && res == 0) {
                res = -1;
            } else if (i > 0 && res > 0) {
                res = 1;
            } else if (i > 0 && res < 0) {
                res = -1;
            } else if (i < 0 && res > 0) {
                res = -1;
            } else if (i < 0 && res < 0) {
                res = 1;
            }
        }
        
        return res;
    }
}