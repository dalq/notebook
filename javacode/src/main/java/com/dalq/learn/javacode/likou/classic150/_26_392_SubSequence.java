package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/22 下午9:10
 */
public class _26_392_SubSequence {
    public boolean isSubsequence(String s, String t) {
        if (s.isEmpty()) {
            return true;
        }
        if (t.isEmpty()) {
            return false;
        }
        
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
            if (i == s.length()) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(new _26_392_SubSequence().isSubsequence("abc", "ahbgdc"));
        System.out.println(new _26_392_SubSequence().isSubsequence("axc", "ahbgdc"));
        System.out.println(new _26_392_SubSequence().isSubsequence("", "ahbgdc"));
        System.out.println("".charAt(0));
    }
}
