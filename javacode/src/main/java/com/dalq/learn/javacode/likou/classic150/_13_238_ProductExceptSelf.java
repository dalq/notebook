package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/31 下午10:01
 */
public class _13_238_ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        int[] res = new int[nums.length];

        left[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        right[nums.length - 1] = 1;
        // watch out! i > -1
        for (int i = nums.length - 2; i > -1; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            res[i] = left[i] * right[i];
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new _13_238_ProductExceptSelf().productExceptSelf(new int[]{1, 2, 3, 4})));
    }
}
