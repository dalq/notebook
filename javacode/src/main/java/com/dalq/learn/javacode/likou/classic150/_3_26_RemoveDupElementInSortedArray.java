package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/25 下午10:23
 */
public class _3_26_RemoveDupElementInSortedArray {
    public static int removeDuplicates(int[] nums) {
        int i = 0;
        int j = i + 1;
        while (j < nums.length) {
            if (nums[i] == nums[j]) {
                nums[i] = nums[j];
                j++;
            } else {
                nums[++i] = nums[j];
                j++;
            }
        }
        System.out.println(Arrays.toString(nums));
        return i + 1;
    }

    public static void main(String[] args) {
        // [0, 1, 4, 0, 3, 0, 4, 2]
        System.out.println(removeDuplicates(new int[]{1, 1, 2, 2, 3, 3, 4}));
    }
}
