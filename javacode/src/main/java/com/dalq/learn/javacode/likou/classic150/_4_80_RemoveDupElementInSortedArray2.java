package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/25 下午11:02
 */
public class _4_80_RemoveDupElementInSortedArray2 {
    /**
     * 双指针法
     * @param nums
     * @return
     */
    public static int removeDuplicates(int[] nums) {
        int i = 0;
        int j = i + 2;
        while (j < nums.length) {
            if (nums[i] == nums[j]) {
                j++;
            } else {
                nums[i + 2] = nums[j];
                i++;
                j++;
            }
        }
        System.out.println(Arrays.toString(nums));
        return i + 2;
    }

    /**
     * 计数法
     * @param nums
     * @return
     */
    public static int removeDuplicates2(int[] nums) {
        int resultIndex = 0;
        int cnt = 1;
//        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (i == nums.length - 1) {
//                result[resultIndex] = nums[i];
                nums[resultIndex] = nums[i];
                break;
            }
            if (nums[i] == nums[i + 1]) {
                cnt++;
                if (cnt <= 2) {
//                    result[resultIndex++] = nums[i];
                    nums[resultIndex++] = nums[i];
                }
            } else {
//                result[resultIndex++] = nums[i];
                nums[resultIndex++] = nums[i];
                cnt = 1;
            }
        }
        System.out.println(Arrays.toString(nums));
        return resultIndex + 1;
    }

    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[]{1,2,3}));
        System.out.println(removeDuplicates2(new int[]{1,1,1,2,2,3}));
    }
}
