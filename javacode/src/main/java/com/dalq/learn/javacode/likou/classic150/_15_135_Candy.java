package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/6/2 下午7:35
 */
public class _15_135_Candy {
    public int candy(int[] ratings) {
        Arrays.sort(ratings);
        int eachCandy = 1;
        int result = 1;
        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                eachCandy++;
            }
            result += eachCandy;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new _15_135_Candy().candy(new int[]{1, 2, 3, 4, 5}));
        System.out.println(new _15_135_Candy().candy(new int[]{1, 0, 2}));
        System.out.println(new _15_135_Candy().candy(new int[]{1, 2, 2}));
    }
}
