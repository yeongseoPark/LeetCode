class Solution {
    public boolean isMonotonic(int[] nums) {
        if (nums.length == 1) return true;

        String mono = null;

        for (int i = 0; i < nums.length - 1; i++) {
            if (mono == null) {
                if (nums[i] == nums[i+1]) continue;
                else if (nums[i] > nums[i+1]) mono = "dec";
                else mono = "inc";                
                }
            else {
                if (mono.equals("inc")) {
                    if (nums[i] > nums[i+1]) return false;
                } else {
                    if (nums[i] < nums[i+1]) return false;
                }
            }
        }

        return true;
    }
}