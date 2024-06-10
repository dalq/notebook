package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/5/28 下午10:26
 */
public class _8_122_MaxStockProfit2 {
    public static int maxProfit(int[] prices) {
        int result = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {
                result += prices[i] - prices[i - 1];
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }
}
