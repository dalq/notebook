package com.dalq.learn.javacode.demo;

import com.google.common.collect.Lists;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

/**
 * @author daling.qdl
 * @date 2024/6/10 上午8:55
 */
public class ResumeInterview {
    public static void main(String[] args) {
        List<String> list = Lists.newArrayList("1", "1", null);
        String str = list.stream().distinct().filter(Objects::nonNull).collect(Collectors.joining(","));
        System.out.println(str);

        List<String> ll = Arrays.asList("1,2,3".split(","));
        System.out.println(ll);

        Integer a = 300;
        Integer b = 300;
        System.out.println("a == b is " + (a==b));
        System.out.println("a.equals(b) is " + a.equals(b));

        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(2);
        queue.add(1);
        System.out.println(queue.peek());
        System.out.println(find("leetcode"));
        System.out.println(String.format("%.2f%%", 0.9 * 100));
    }

    public static int find(String input) {
        // your code
        if (input == null || input.length() == 0) {
            return -1;
        }
        int[] countArray = new int[256];
        for (int i = 0; i < input.length(); i ++) {
            countArray[input.charAt(i)] ++;//这行代码有问题吗
        }
        for (int i = 0; i < input.length(); i ++) {
            if (countArray[input.charAt(i)] == 1) {
                return i;
            }
        }
        return -1;
    }
}
