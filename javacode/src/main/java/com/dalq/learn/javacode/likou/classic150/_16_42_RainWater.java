package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/4 下午10:36
 */
public class _16_42_RainWater {
    public int trap(int[] height) {
        int n = height.length;
        int result = 0;
        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        
        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
        }
        
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i > -1; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i]);
        }
        
        for (int i = 0; i < n; i++) {
            result += Math.min(leftMax[i], rightMax[i]) - height[i];
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(new _16_42_RainWater().trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
        System.out.println(new _16_42_RainWater().trap(new int[]{1,0,1}));
    }
}
