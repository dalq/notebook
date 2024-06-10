package com.dalq.learn.javacode.likou.classic150;

import java.util.HashMap;
import java.util.Map;

/**
 * @author daling.qdl
 * @date 2024/6/6 下午10:20
 */
public class _17_13_RomanToInt {
    public int romanToInt(String s) {
        Map<String, Integer> map = new HashMap<>();
        map.put("I", 1);
        map.put("IV", 4);
        map.put("V", 5);
        map.put("IX", 9);
        map.put("X", 10);
        map.put("XL", 40);
        map.put("L", 50);
        map.put("XC", 90);
        map.put("C", 100);
        map.put("CD", 400);
        map.put("D", 500);
        map.put("CM", 900);
        map.put("M", 1000);
        
        if (s.length() <= 1) {
            return map.get(s);
        }
        
        int i = s.length() - 1;
        int result = 0;
        while (i >= 0) {
            if (i == 0) {
                result += map.get(s.substring(0, 1));
                break;
            }
            if (map.get(s.substring(i - 1, i + 1)) != null) {
                result += map.get(s.substring(i - 1, i + 1));
                i -= 2;
            } else {
                result += map.get(s.substring(i, i + 1));
                i--;
            }
        }
        return result;
    }

    public int romanToInt2(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        map.put('v', 4);
        map.put('x', 9);
        map.put('l', 40);
        map.put('c', 90);
        map.put('d', 400);
        map.put('m', 900);

        String replace = s.replace("IV", "v").replace("IX", "x").replace("XL", "l").replace("XC", "c").replace("CD", "d").replace("CM", "m");
        
        int result = 0;
        for (char c : replace.toCharArray()) {
            result += map.get(c);
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new _17_13_RomanToInt().romanToInt2("III"));
        System.out.println(new _17_13_RomanToInt().romanToInt2("IV"));
        System.out.println(new _17_13_RomanToInt().romanToInt2("IX"));
        System.out.println(new _17_13_RomanToInt().romanToInt2("LVIII"));
        System.out.println(new _17_13_RomanToInt().romanToInt2("MCMXCIV"));
    }
}
