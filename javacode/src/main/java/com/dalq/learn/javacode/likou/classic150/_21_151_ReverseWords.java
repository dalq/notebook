package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/10 下午2:32
 */
public class _21_151_ReverseWords {
    public String reverseWords(String s) {
        String[] words = s.trim().split(" +");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i > -1; i--) {
            sb.append(words[i]).append(" ");
        }
        return sb.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(new _21_151_ReverseWords().reverseWords("the sky is blue"));
        System.out.println(new _21_151_ReverseWords().reverseWords("  hello world  "));
        System.out.println(new _21_151_ReverseWords().reverseWords("a good   example"));
    }
}
