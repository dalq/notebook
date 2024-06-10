package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/5/27 下午10:32
 */
public class _7_121_MaxStockProfit {

    public static int maxProfit(int[] prices) {
        int result = 0;
        int tmpMin = Integer.MAX_VALUE;
        for (int price : prices) {
            tmpMin = Math.min(tmpMin, price);
            result = Math.max(result, price - tmpMin);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("result == " + maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }
}
