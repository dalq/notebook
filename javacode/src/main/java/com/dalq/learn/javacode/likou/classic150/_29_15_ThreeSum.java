package com.dalq.learn.javacode.likou.classic150;

import com.google.common.collect.Lists;

import java.util.*;

/**
 * @author daling.qdl
 * @date 2024/6/24 下午10:02
 */
public class _29_15_ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            int target = -nums[i];
            List<List<Integer>> subList = twoSum(nums, i + 1, target);
            if (!subList.isEmpty()) {
                result.addAll(subList);
            }
            while (i < nums.length - 1 && nums[i] == nums[i + 1]) {
                i++;
            }
        }
        return result;
    }

    /**
     * 子函数-2sum加去重
     * @param nums
     * @param subIndex
     * @param target
     * @return
     */
    public List<List<Integer>> twoSum(int[] nums, int subIndex, int target) {
        List<List<Integer>> result = new ArrayList<>();
        int low = subIndex, high = nums.length - 1;
        while (low < high) {
            int numLow = nums[low];
            int numHigh = nums[high];
            if (numLow + numHigh == target) {
//                result.add(List.of(nums[low], nums[high]));
                result.add(List.of(-target, nums[low], nums[high]));
                while (low < high && nums[low] == nums[low + 1]) {
                    low++;
                }
                while (low < high && nums[high] == nums[high - 1]) {
                    high--;
                }
                low++;
                high--;
            } else if (numLow + numHigh < target) {
                low++;
            } else if (numLow + numHigh > target) {
                high--;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new _29_15_ThreeSum().threeSum(new int[]{-1, 0, 1, 2, -1, -4}));
        System.out.println(new _29_15_ThreeSum().threeSum(new int[]{0, 1, 1}));
        System.out.println(new _29_15_ThreeSum().threeSum(new int[]{0, 0, 0}));


//        System.out.println(new _29_15_ThreeSum().twoSum(new int[]{1,1,3,5,6,6,8}, 1, 9));
        
    }
}
