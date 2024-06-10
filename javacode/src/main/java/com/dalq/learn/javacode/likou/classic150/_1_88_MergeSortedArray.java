package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * 1、偷懒解法：append然后Arrays.sort
 * 2、实际考察解法：双指针法
 * @author daling.qdl
 * @date 2024/5/25 下午8:27
 */
public class _1_88_MergeSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n <= 0) {
            return;
        }
        int[] result = new int[m + n];
        int i = 0;
        int j = 0;
        for (int k = 0; k < m + n; k++) {
            if (nums1[i] <= nums2[j] && i < m) {
                result[k] = nums1[i];
                i++;
            } else if (nums1[i] > nums2[j] && j < n) {
                result[k] = nums2[j];
                j++;
            } else if (i < m) {
                result[k] = nums1[i];
                i++;
            } else if (j < n) {
                result[k] = nums2[j];
                j++;
            }
        }
        for (int l = 0; l < m + n; l++) {
            nums1[l] = result[l];
        }
    }

    public static void main(String[] args) {
        int[] nums1 = {0};
        int[] nums2 = {};
        int m = 1;
        int n = 0;
        merge(nums1, m, nums2, n);
        System.out.println(Arrays.toString(nums1));
    }
}
