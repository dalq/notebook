package com.dalq.learn.javacode.likou.classic150;

/**
 * 总和大于等于 target 的长度最小的子数组，并返回其长度
 *
 * @author daling.qdl
 * @date 2024/6/28 下午9:58
 */
public class _30_209_MinSubArrayLen {

    public int minSubArrayLen(int target, int[] nums) {
        int result = Integer.MAX_VALUE;
        int i = 0;
        int sum = 0;
        for (int j = 0; j < nums.length; j++) {
            sum += nums[j];
            while (sum >= target) {
                result = Math.min(result, j - i + 1);
                sum = sum - nums[i];
                i++;
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }
    public int minSubArrayLen_timeout(int target, int[] nums) {
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum >= target) {
                    result = Math.min(result, j - i + 1);
                    break;
                }
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }

    public static void main(String[] args) {
        System.out.println(new _30_209_MinSubArrayLen().minSubArrayLen(7, new int[]{2, 3, 1, 2, 4, 3}));
        System.out.println(new _30_209_MinSubArrayLen().minSubArrayLen(4, new int[]{1, 4, 4}));
        System.out.println(new _30_209_MinSubArrayLen().minSubArrayLen(11, new int[]{1, 1, 1, 1, 1, 1, 1, 1}));
        System.out.println(new _30_209_MinSubArrayLen().minSubArrayLen(6, new int[]{10, 2, 3}));
        System.out.println(new _30_209_MinSubArrayLen().minSubArrayLen(15, new int[]{5,1,3,5,10,7,4,9,2,8}));
    }
}
