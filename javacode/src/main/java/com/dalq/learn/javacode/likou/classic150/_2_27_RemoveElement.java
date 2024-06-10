package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/25 下午9:37
 */
public class _2_27_RemoveElement {
    public static int removeElement(int[] nums, int val) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            if (nums[start] == val) {
                nums[start] = nums[end--];
            } else {
                start++;
            }
        }
        return start;
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 2, 3};
        removeElement(nums, 3);
        System.out.println(Arrays.toString(nums));

        int[] num2 = {0,1,2,2,3,0,4,2};
        removeElement(num2, 2);
        System.out.println(Arrays.toString(num2));
    }
}
