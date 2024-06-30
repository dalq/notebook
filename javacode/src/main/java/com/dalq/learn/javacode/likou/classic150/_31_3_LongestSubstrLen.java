package com.dalq.learn.javacode.likou.classic150;

import ch.qos.logback.core.encoder.JsonEscapeUtil;

import java.util.HashMap;
import java.util.Map;

/**
 * 出不含有重复字符的最长子串长度
 * @author daling.qdl
 * @date 2024/6/29 下午7:15
 */
public class _31_3_LongestSubstrLen {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.isEmpty()) {
            return 0;
        }
        int i = 0;
        int result = Integer.MIN_VALUE;
        Map<Character, Integer> map = new HashMap<>();
        for (int j = 0; j <= s.length() - 1; j++) {
            char c = s.charAt(j);
            Integer index = map.get(c);
            if (index == null || index < i) {
                map.put(c, j);
                result = Math.max(result, j - i + 1);
            } else {
                i = index + 1;
                map.put(c, j);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new _31_3_LongestSubstrLen().lengthOfLongestSubstring("abcabcbb"));
        System.out.println(new _31_3_LongestSubstrLen().lengthOfLongestSubstring("bbbbb"));
        System.out.println(new _31_3_LongestSubstrLen().lengthOfLongestSubstring("pwwkew"));
        System.out.println(new _31_3_LongestSubstrLen().lengthOfLongestSubstring("aaaabccc"));
        System.out.println(new _31_3_LongestSubstrLen().lengthOfLongestSubstring("tmmzuxt"));
    }
}
