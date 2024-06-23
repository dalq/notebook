package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/23 下午8:46
 */
public class _28_11_MaxArea {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int area = 0;
        while (left <= right) {
            int min = Math.min(height[left], height[right]);
            area = Math.max(area, min * (right - left));
            if (height[left] <= height[right]) {
                left++;
            } else if (height[left] > height[right]){
                right--;
            }
        }
        return area;
    }

    public static void main(String[] args) {
        System.out.println(new _28_11_MaxArea().maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));
    }
}
