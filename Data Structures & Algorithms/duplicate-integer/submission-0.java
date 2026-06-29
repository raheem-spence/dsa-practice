class Solution {
    public boolean hasDuplicate(int[] nums) {

        

        for (int i = 0; i < nums.length; i++) {
            int currentNum = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                if (currentNum == nums[j]){
                    return true;
                }

            }
        }
        return false;
        
    }
}