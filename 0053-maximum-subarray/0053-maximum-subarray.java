class Solution {
    public int maxSubArray(int[] nums) {
        int answer = Integer.MIN_VALUE;
        int max = 0;
        for(int num : nums){
            max += num;
            answer = Math.max(answer, max);
            max = Math.max(max, 0);
        }
        return answer;
    }
}