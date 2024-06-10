package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/5/30 下午10:00
 */
public class _11_274_HIndex {
    public static int hIndex(int[] citations) {
        if (citations.length == 1) {
            return citations[0] == 0 ? 0 : 1;
        }
        Arrays.sort(citations);
        int result = 0;
        for (int i = 0; i < citations.length; i++) {
            // 第1、2、3、……个后向遍历的元素
            int reverseIndex = i + 1;
            // 第1、2、3、……个后向遍历的元素里放的值
            int cur = citations[citations.length - 1 - i];

            // 边界情况
            if (cur <= 0) {
                return result;
            }

            // 如果遍历排序都大于了当前遍历到的值，由于数组是有序的，后边肯定没戏，直接返回
            if (reverseIndex > cur) {
                return result;
            } else {
                result = reverseIndex;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(hIndex(new int[]{4, 4, 0, 0}));
    }
}
