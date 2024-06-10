package com.dalq.learn.javacode.likou.classic150;

/**
 * @author daling.qdl
 * @date 2024/6/8 下午7:44
 */
public class _18_12_IntToRoman {
    public String intToRoman(int num) {
        StringBuilder roman = new StringBuilder();

        int qian = num / 1000;
        while (qian > 0) {
            roman.append("M");
            qian--;
        }

        int bai = num % 1000 / 100;
        if (bai == 9) {
            roman.append("CM");
        } else if (bai >= 5) {
            roman.append("D");
            int bai5 = bai - 5;
            while (bai5 > 0) {
                roman.append("C");
                bai5--;
            }
        } else if (bai == 4) {
            roman.append("CD");
        } else {
            while (bai > 0) {
                roman.append("C");
                bai--;
            }
        }
        
        int shi = num % 1000 % 100 / 10;
        if (shi == 9) {
            roman.append("XC");
        } else if (shi >= 5) {
            roman.append("L");
            int shi5 = shi - 5;
            while (shi5 > 0) {
                roman.append("X");
                shi5--;
            }
        } else if (shi == 4) {
            roman.append("XL");
        } else {
            while (shi > 0) {
                roman.append("X");
                shi--;
            }
        }
        
        int ge = num % 1000 % 100 % 10;
        if (ge == 9) {
            roman.append("IX");
        } else if (ge >= 5) {
            roman.append("V");
            int ge5 = ge - 5;
            while (ge5 > 0) {
                roman.append("I");
                ge5--;
            }
        } else if (ge == 4) {
            roman.append("IV");
        } else {
            while (ge > 0) {
                roman.append("I");
                ge--;
            }
        }
                
        return roman.toString();
    }

    public static void main(String[] args) {
        System.out.println(new _18_12_IntToRoman().intToRoman(3749));
        System.out.println(new _18_12_IntToRoman().intToRoman(58));
        System.out.println(new _18_12_IntToRoman().intToRoman(1994));
        System.out.println(new _18_12_IntToRoman().intToRoman(60));
    }
}
