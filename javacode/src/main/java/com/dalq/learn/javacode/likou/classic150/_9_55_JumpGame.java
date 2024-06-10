package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/5/28 下午11:25
 */
public class _9_55_JumpGame {
    public static boolean canJump(int[] nums) {
        int maxIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (maxIndex < i) {
                return false;
            }
            maxIndex = Math.max(maxIndex, i + nums[i]);
            if (maxIndex >= nums.length - 1) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
//        System.out.println(canJump(new int[]{2, 3, 1, 1, 4}));
        System.out.println(canJump(new int[]{3,2,1,0,4}));
    }
}
