package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/26 下午10:56
 */
public class _6_189_RotateArray {
    public static void rotate(int[] nums, int k) {
        if (nums.length <= 1) {
            return;
        }
        if (nums.length < k) {
            k = k % nums.length;
        }
        
        int[] tmp = new int[nums.length - k];
        System.arraycopy(nums, 0, tmp, 0, nums.length - k);
        System.arraycopy(nums, nums.length - k, nums, 0, k);
        System.arraycopy(tmp, 0, nums, k, nums.length - k);
    }

    public static void main(String[] args) {
        int[] nums = new int[] {-1,-100,3,99};
        rotate(nums, 2);
        System.out.println(Arrays.toString(nums));
    }
}
