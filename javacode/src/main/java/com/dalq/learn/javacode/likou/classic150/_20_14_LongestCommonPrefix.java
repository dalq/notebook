package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/9 下午8:05
 */
public class _20_14_LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder sb = new StringBuilder();
        char tmp = ' ';
        int i = 0;
        while (i < strs[0].length()) {
            for (String str : strs) {
                if (i == str.length()) {
                    return sb.toString();
                }
                if (tmp == ' ') {
                    tmp = str.charAt(i);
                }
                if (tmp != str.charAt(i)) {
                    return sb.toString();
                }
            }
            sb.append(tmp);
            tmp = ' ';
            i++;
        }
        return sb.toString();
    }

    public String longestCommonPrefix2(String[] strs) {
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            for (String str : strs) {
                if (i == str.length() || str.charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }

    public static void main(String[] args) {
        System.out.println(new _20_14_LongestCommonPrefix().longestCommonPrefix(new String[]{"flower","flow","flow","flight"}));
        System.out.println(new _20_14_LongestCommonPrefix().longestCommonPrefix(new String[]{"dog","racecar","car"}));

        System.out.println(new _20_14_LongestCommonPrefix().longestCommonPrefix2(new String[]{"flower","flow","flow","flight"}));
        System.out.println(new _20_14_LongestCommonPrefix().longestCommonPrefix2(new String[]{"dog","racecar","car"}));
    }
}
