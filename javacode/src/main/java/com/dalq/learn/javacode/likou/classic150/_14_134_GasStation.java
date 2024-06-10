package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/1 下午8:21
 */
public class _14_134_GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        for (int i = 0; i < gas.length; i++) {
            int j = i;
            int remain = gas[j];
            while (remain - cost[j] >= 0) {
                remain = remain - cost[j] + gas[(j + 1) % n];
                // 全场最佳
                j = (j + 1) % n;
                if (j == i) {
                    return j;
                }
            }
            // 不考虑耗时性能优化，能写出这样子的代码就已经挺牛逼的了我认为
        }
        return -1;
    }

    public static void main(String[] args) {
            System.out.println(new _14_134_GasStation().canCompleteCircuit(new int[]{1,2,3,4,5}, new int[]{3,4,5,1,2}));
            System.out.println(new _14_134_GasStation().canCompleteCircuit(new int[]{2,3,4}, new int[]{3,4,3}));
            System.out.println(new _14_134_GasStation().canCompleteCircuit(new int[]{4,5,2,6,5,3}, new int[]{3,2,7,3,2,9}));
    }
}
