package com.dalq.learn.javacode.likou.classic150;

import java.util.Arrays;

/**
 * @author daling.qdl
 * @date 2024/6/22 下午6:48
 */
public class _25_125_Palindrome {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(Character.toLowerCase(c));
            }
        }
        String filterStr = sb.toString();
        String reverseStr = sb.reverse().toString();
        return filterStr.equals(reverseStr);
    }

    public static void main(String[] args) {
//        System.out.println(new _25_125_Palindrome().isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(new _25_125_Palindrome().isPalindrome("0P"));
    }
}
