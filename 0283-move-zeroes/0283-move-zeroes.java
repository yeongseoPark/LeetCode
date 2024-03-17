class Solution {
    
    public void moveZeroes(int[] nums) {
        int snowBallSize = 0;
        for (int i=0; i < nums.length; i++) {
            if (nums[i] == 0) {
                snowBallSize += 1;
            }
            else if (snowBallSize > 0) {
                int tmp = nums[i];
                nums[i] = 0;
                nums[i - snowBallSize] = tmp;
            }
        }
    }
}