package com.dalq.learn.javacode.likou.classic150;

import com.google.common.collect.Lists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author daling.qdl
 * @date 2024/6/16 下午9:23
 */
public class _24_68_TextFullJustify {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        
        for (int i = 0; i < words.length;) {
            int currentLen = words[i].length() + 1;
            // 1、这一行就一个单词（单词长度占满一行 or 到了最后一个单词）
            if (currentLen >= maxWidth || i == words.length - 1) {
                result.add(oneWord(words[i], maxWidth));
                i++;
                continue;
            }
            
            for (int j = i + 1; j < words.length; j++) {
                currentLen += words[j].length() + 1;
                
                // 2、最后一行，左对齐分布（注意&&之前的判断）
                if (currentLen <= maxWidth && j == words.length - 1) {
                    result.add(lastRow(words, i, maxWidth));
                    i = j + 1;
                    break;
                }
                
                if (currentLen < maxWidth && j < words.length - 1) {
                    continue;
                }
                // 3、普通行，子串们刚好占满宽度，则居中均匀分布
                if (currentLen == maxWidth || currentLen == maxWidth + 1) {
                    result.add(middleRow(words, i, j, maxWidth));
                    i = j + 1;
                    break;
                }
                // 3、普通行，子串们第一次超出了宽度，则取前一个子串并居中均匀分布
                if (currentLen >= maxWidth + 1) {
                    result.add(middleRow(words, i, j - 1, maxWidth));
                    i = j;
                    break;
                }
            }
            
        }
        return result;
    }

    private String oneWord(String word, int maxWidth) {
        StringBuilder result = new StringBuilder(word);
        while (result.length() < maxWidth) {
            result.append(" ");
        }
        return result.toString();
    }

    private String middleRow(String[] words, int start, int end, int maxWidth) {
        List<String> subList = Arrays.asList(words).subList(start, end + 1);
        int len = subList.stream().mapToInt(String::length).sum();
        int averageBlankCnt;
        int averageBlankRatio;
        if (subList.size() == 1) {
            averageBlankCnt = maxWidth - subList.get(0).length();
            averageBlankRatio = 0;
        } else {
            averageBlankCnt = (maxWidth - len) / (subList.size() - 1);
            averageBlankRatio = (maxWidth - len) % (subList.size() - 1);
        }

        StringBuilder sb = new StringBuilder();
        // 最后一个单词不加空格
        for (int i = 0; i < subList.size(); i++) {
            // 这里无脑加空格，即使超了最后的subString会兜底
            sb.append(subList.get(i)).append(" ".repeat(i <= averageBlankRatio - 1 ? averageBlankCnt + 1 : averageBlankCnt));
        }
        
        return sb.substring(0, maxWidth);
    }
    
    private String lastRow(String[] words, int start, int maxWidth) {
        StringBuilder result = new StringBuilder();
        for (int i = start; i < words.length; i++) {
            result.append(words[i]).append(" ");
        }
        while (result.length() < maxWidth) {
            result.append(" ");
        }
        return result.toString();
    }

    public static void main(String[] args) {
//        System.out.println(new _24_68_TextFullJustify().lastRow(new String[]{"a", "b", "c"}, 0, 7));
//        System.out.println(new _24_68_TextFullJustify().middleRow(new String[]{"example", "of", "text"}, 0, 2, 16));
//        System.out.println(new _24_68_TextFullJustify().fullJustify(new String[]{"What","must","be","acknowledgment","shall","be"}, 16));
//        System.out.println(new _24_68_TextFullJustify().fullJustify(new String[]{"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"}, 20));
        System.out.println(new _24_68_TextFullJustify().fullJustify(new String[]{"a","b","c","d","e","f"}, 6));
    }
}
