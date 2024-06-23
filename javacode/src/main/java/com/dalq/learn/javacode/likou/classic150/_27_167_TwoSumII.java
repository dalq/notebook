package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/6/22 下午11:21
 */
public class _27_167_TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length - 1; i++) {
            int one = numbers[i];
            int minus = target - one;
            if (minus < one) {
                continue;
            }
            int low = i + 1, high = numbers.length - 1;
            while (low <= high) {
                int middle = low + (high - low) / 2;
                if (numbers[middle] == minus) {
                    return new int[]{i + 1, middle + 1};
                } else if (numbers[middle] > minus) {
                    high = middle - 1;
                } else if (numbers[middle] < minus) {
                    low = middle + 1;
                }
            }
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new _27_167_TwoSumII().twoSum(new int[]{2, 7, 11, 15}, 9)));
        System.out.println(Arrays.toString(new _27_167_TwoSumII().twoSum(new int[]{2,3,4}, 6)));
        System.out.println(Arrays.toString(new _27_167_TwoSumII().twoSum(new int[]{-1, 0}, -1)));
    }
}
