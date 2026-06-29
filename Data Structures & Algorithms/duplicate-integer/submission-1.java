class Solution {
    public boolean hasDuplicate(int[] nums) {

        // Create a set for ints from nums array
        Set<Integer> numberSet = new HashSet<>();

        for (int num : nums) {
            numberSet.add(num);
        }

        return nums.length != numberSet.size();
    }
    
}