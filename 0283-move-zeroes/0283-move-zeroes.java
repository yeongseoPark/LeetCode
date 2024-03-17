class Solution {
    public void pull(int[] nums, int idx) {
        for (int i = idx + 1; i < nums.length; i++) {
            nums[i-1] = nums[i];
        }
    }
    public void moveZeroes(int[] nums) {
        int i = 0;
        int zeroCnt = 0;

        while (true) {
            if (i == nums.length - zeroCnt) {
                break;
            }


            if (nums[i] == 0) {
                zeroCnt++;
                pull(nums, i);
                nums[nums.length - 1] = 0;
                continue;
            }
            i++;
        }
    }
}