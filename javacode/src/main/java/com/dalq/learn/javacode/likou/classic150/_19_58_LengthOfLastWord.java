package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/9 下午7:57
 */
public class _19_58_LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        String[] split = s.trim().split(" ");
        return split[split.length - 1].length();
    }

    public static void main(String[] args) {
        System.out.println(new _19_58_LengthOfLastWord().lengthOfLastWord(" "));
        System.out.println(new _19_58_LengthOfLastWord().lengthOfLastWord("Hello World"));
        System.out.println(new _19_58_LengthOfLastWord().lengthOfLastWord("   fly me   to   the moon  "));
        System.out.println(new _19_58_LengthOfLastWord().lengthOfLastWord("luffy is still joyboy"));
    }
}
