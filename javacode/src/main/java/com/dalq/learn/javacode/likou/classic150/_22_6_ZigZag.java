package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/11 下午10:53
 */
public class _22_6_ZigZag {
    public String convert(String s, int numRows) {
        StringBuilder[] sbArray = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            sbArray[i] = new StringBuilder();
        }
        
        int i = 0;
        boolean flag = true;
        while (i < s.length()) {
            if (flag) {
                for (int j = 0; j < numRows && i < s.length(); j++) {
                    sbArray[j].append(s.charAt(i++));
                }
                flag = false;
            } else {
                for (int j = numRows - 2; j > 0 && i < s.length(); j--) {
                    sbArray[j].append(s.charAt(i++));
                }
                flag = true;
            }
        }
        
        StringBuilder res = new StringBuilder();
        for (StringBuilder sb : sbArray) {
            res.append(sb);
        }
        return res.toString();
    }

    public static void main(String[] args) {
        System.out.println(new _22_6_ZigZag().convert("PAYPALISHIRING", 3));
        System.out.println(new _22_6_ZigZag().convert("PAYPALISHIRING", 4));
        System.out.println(new _22_6_ZigZag().convert("A", 1));
    }
}
