import java.io.*;
import java.util.*;

/**
 * @author daling.qdl
 * @date 2017/06/18
 * @since 2017/6/18 18:01
 */
public class RfqWords {

    private static Map<String, Integer> COUNT_MAP = new HashMap<String, Integer>();
    private static Set<String>          WORDS_SET = new HashSet<String>();

    public static void main(String[] args) throws IOException {

        doJob("/Users/quan/study/code/src/main/resources/RFQInput.txt",
              "/Users/quan/study/code/src/main/resources/Dictionary_100M_final.txt",
              "/Users/quan/study/code/src/main/resources/Result.csv");

    }

    private static void doJob(String rfqContentFilePath, String wordsFilePath,
                              String resultCSVFilePath) throws IOException {
        // 获取开始时间
        long startTime = System.currentTimeMillis();

        // 读取字典
        File wordFile = new File(wordsFilePath);
        Long wordFileLength = wordFile.length();
        byte[] wordFileContent = new byte[wordFileLength.intValue()];
        FileInputStream wordIn = new FileInputStream(wordFile);
        wordIn.read(wordFileContent);
        wordIn.close();

        // 读取RFQ
        File rfqFile = new File(rfqContentFilePath);
        Long rfqFileLength = rfqFile.length();
        byte[] rfqFileContent = new byte[rfqFileLength.intValue()];
        FileInputStream rfqIn = new FileInputStream(rfqFile);
        rfqIn.read(rfqFileContent);
        rfqIn.close();
        //System.out.println("读文件耗时： " + (System.currentTimeMillis() - startTime) + "ms");

        // 构造词典树
        TireTree trie = new TireTree();
        String tmp = null;
        for (int i = 0, j = 0; i < wordFileLength; i++) {
            if (wordFileContent[i] == ',') {
                tmp = new String(wordFileContent, j, i - j);
                WORDS_SET.add(tmp);
                String[] ws = tmp.split(" ");
                for (String w : ws) {
                    trie.insert(w);
                }
            }
            j = i;
        }

//        String[] words = new String(wordFileContent).split(",");
//        for (String word : words) {
//            WORDS_SET.add(word);
//            String[] ws = word.split(" ");
//            for (String w : ws) {
//                trie.insert(w);
//            }
//        }
        System.out.println("构造字典树耗时： " + (System.currentTimeMillis() - startTime) + "ms");

        // RFQ预处理
        List<String> preRfq = new ArrayList<String>();
        StringBuilder sb = new StringBuilder();
        boolean badWords = false;
        for (byte aRfqFileContent : rfqFileContent) {
            byte c = aRfqFileContent;
            if (c >= 'A' && c <= 'Z') {
                if (badWords) {
                    continue;
                }
                c += 32;
            }
            if (c >= 'a' && c <= 'z') {
                if (badWords) {
                    continue;
                }
                sb.append((char) c);
            } else if (c >= '0' && c <= '9') {
                badWords = true;
            } else {
                if (sb.length() > 0) {
                    preRfq.add(sb.toString());
                    sb.delete(0, sb.length());
                }
                badWords = false;
            }
        }
        //System.out.println("RFQ预处理耗时： " + (System.currentTimeMillis() - startTime) + "ms");

        // 查字典
        // 字典中最多三个单词
        String ss = null;
        String ss1 = null;
        String ss2 = null;
        int ll = preRfq.size();
        for (int i = 0; i < ll; ) {
            ss = preRfq.get(i);
            if (trie.isExist(ss)) {
                if (WORDS_SET.contains(ss)) {
                    updateMap(ss);
                } else {
                    if (i + 1 >= preRfq.size() - 1) {
                        i++;
                        continue;
                    }
                    ss1 = preRfq.get(i + 1);
                    if (trie.isExist(ss1)) {
                        if (WORDS_SET.contains(ss + " " + ss1)) {
                            updateMap(ss + " " + ss1);
                        } else {
                            if (i + 2 >= preRfq.size() - 1) {
                                i++;
                                continue;
                            }
                            ss2 = preRfq.get(i + 2);
                            if (trie.isExist(ss2)) {
                                if (WORDS_SET.contains(ss + " " + ss1 + " " + ss2)) {
                                    updateMap(ss + " " + ss1 + " " + ss2);
                                }
                            }
                        }
                    }
                }
            }
            i++;
        }
        //System.out.println("查字典耗时： " + (System.currentTimeMillis() - startTime) + "ms");

        // 写结果
        File resultFile = new File(resultCSVFilePath);
        FileWriter fw = new FileWriter(resultFile);
        BufferedWriter writer = new BufferedWriter(fw);
        for (Map.Entry<String, Integer> entry : COUNT_MAP.entrySet()) {
            writer.write(entry.getKey() + "," + entry.getValue());
            writer.newLine();// 换行
        }
        writer.flush();
        fw.close();

        // 获取结束时间
        System.out.println("程序运行时间： " + (System.currentTimeMillis() - startTime) + "ms");
    }

    private static void updateMap(String word) {
        if (COUNT_MAP.containsKey(word)) {
            int count = COUNT_MAP.get(word);
            count++;
            COUNT_MAP.put(word, count);
        } else {
            COUNT_MAP.put(word, 1);
        }
    }

    /**
     * tire词典树类
     *
     * @see <a href="http://blog.csdn.net/abcd_d_/article/details/40116485"> java实现的Trie树数据结构</a>
     */
    private static class TireTree {

        /**
         * 内部节点类
         *
         * @author "zhshl"
         * @date 2014-10-14
         */
        private class Node {

            // 此处用数组实现，当然也可以map或list实现以节省空间
            private Node    childs[];

            Node() {
                childs = new Node[26];
            }
        }

        // 树根
        private Node root;

        TireTree() {
            /// 初始化trie 树
            root = new Node();
        }

        /**
         * 插入字串，用循环代替迭代实现
         *
         * @param words
         */
        public void insert(String words) {
            insert(this.root, words);
        }

        /**
         * 插入字串，用循环代替迭代实现
         *
         * @param root
         * @param words
         */
        private void insert(Node root, String words) {
            // 转化为小写
            //words = words.toLowerCase();
            char[] chrs = words.toCharArray();

            for (int i = 0, length = chrs.length; i < length; i++) {
                /// 用相对于a字母的值作为下标索引，也隐式地记录了该字母的值
                int index = chrs[i] - 'a';
                if (root.childs[index] == null) {
                    root.childs[index] = new Node();
                }
                /// root指向子节点，继续处理
                root = root.childs[index];
            }

        }

        /**
         * 判断某字串是否在字典树中
         *
         * @param word
         * @return true if exists ,otherwise false
         */
        public boolean isExist(String word) {
            return search(this.root, word);
        }

        /**
         * 查询某字串是否在字典树中
         *
         * @param word
         * @return true if exists ,otherwise false
         */
        private boolean search(Node root, String word) {
            char[] chs = word.toLowerCase().toCharArray();
            for (int i = 0, length = chs.length; i < length; i++) {
                int index = chs[i] - 'a';
                if (root.childs[index] == null) {
                    /// 如果不存在，则查找失败
                    return false;
                }
                root = root.childs[index];
            }

            return true;
        }
    }

}
