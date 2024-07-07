package com.dalq.learn.javacode.likou.classic150;

import java.util.HashMap;
import java.util.Map;

/**
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
 * @author daling.qdl
 * @date 2024/7/6 下午8:28
 */
public class _33_76_MinWindow {
    public String minWindow(String s, String t) {
        if (s.length() <= 1) {
            return s.equals(t) ? s : "";
        }
        if (t.length() <= 1) {
            return !s.contains(t) ? "" : t;
        }
        
        Map<Character, Integer> tMap = new HashMap<>();
        for (char tc : t.toCharArray()) {
            tMap.put(tc, tMap.getOrDefault(tc, 0) + 1);
        }
        
        int i = 0, j = 1, targetI = 0, targetJ = 0;
        int currentSize = Integer.MAX_VALUE;
        while (i < s.length() - 1 && j < s.length() + 1) {
            j = i + 1;
            while (j < s.length() + 1) {
                int match = match(s, i, j, tMap);
                if (match > i) {
                    if (j - i < currentSize) {
                        currentSize = j - i;
                        targetI = i;
                        targetJ = j;
                    }
                    i = match;
                    break;
                } else {
                    j++;
                }
            }
        }
        
        return currentSize == Integer.MAX_VALUE ? "" : s.substring(targetI, targetJ);
    }

    public String minWindow2(String s, String t) {
        if (s.length() <= 1) {
            return s.equals(t) ? s : "";
        }
        if (t.length() <= 1) {
            return !s.contains(t) ? "" : t;
        }

        Map<Character, Integer> tMap = new HashMap<>();
        for (char tc : t.toCharArray()) {
            tMap.put(tc, tMap.getOrDefault(tc, 0) + 1);
        }

        int targetI = 0, targetJ = 0, need = t.length(), currentSize = Integer.MAX_VALUE;
        for (int i = 0, j = 0; j < s.length(); j++) {
            char rightC = s.charAt(j);
            if (tMap.getOrDefault(rightC, 0) > 0) {
                need--;
                // 不是在if里哦
                //tMap.put(c, tMap.getOrDefault(c, 0) - 1);
            }
            // 非t中的字符，可能会被减为负数
            tMap.put(rightC, tMap.getOrDefault(rightC, 0) - 1);
            if (need == 0) {
                //移动左指针的逻辑
                while (true) {
                    char leftC = s.charAt(i);
                    if (tMap.get(leftC) == 0) {
                        break;
                    }
                    // 🔥缩小左边界，该字符所需要的数量+1
                    // 主要是上面提前break了，所以break的那次下面两行代码无法执行到，所以还需要90-92的重复代码
                    tMap.put(leftC, tMap.getOrDefault(leftC, 0) + 1);
                    i++;
                }
                if (j - i + 1 < currentSize) {
                    currentSize = j - i + 1;
                    targetI = i;
                    targetJ = j;
                }
                //🔥将左边界右移,执行下一个窗口，由于左边界是t需要的字符，右移后，需要更新tMap和needCnt，表示还需要增加一个字符
                char nextLeftC = s.charAt(i);
                tMap.put(nextLeftC, tMap.getOrDefault(nextLeftC, 0) + 1);
                need++;
                i++;
            }
        }
        
        return currentSize == Integer.MAX_VALUE ? "" : s.substring(targetI, targetJ + 1);
    }

    /**
     * 如果匹配返回s中第一个命中的字母
     * @param s
     * @param start
     * @param end
     * @param targetMap
     * @return
     */
    private int match(String s, int start, int end, Map<Character, Integer> targetMap) {
        Map<Character, Integer> subStrMap = new HashMap<>();
        int firstMatchIndex = -1;
        for (int i = start; i < end; i++) {
            char c = s.charAt(i);
            if (firstMatchIndex <= start && targetMap.containsKey(c)) {
                firstMatchIndex = i;
            }
            subStrMap.put(c, subStrMap.getOrDefault(c, 0) + 1);
        }
        
        for (Map.Entry<Character, Integer> entry : targetMap.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            if (!subStrMap.containsKey(key) || subStrMap.get(key) < value) {
                return -1;
            }
        }
        return firstMatchIndex;
    }

    public static void main(String[] args) {
        System.out.println(new _33_76_MinWindow().minWindow2("ab", "a"));
        System.out.println(new _33_76_MinWindow().minWindow2("ADOBECODE", "ABC"));
        System.out.println(new _33_76_MinWindow().minWindow2("ADOBECODEBANC", "ABC"));
    }
}
