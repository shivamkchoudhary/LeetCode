class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE;
        int currSum = 0;
        for (int i : nums) {
            currSum = Math.max(currSum, 0);
            currSum += i;
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
        
    }
}
