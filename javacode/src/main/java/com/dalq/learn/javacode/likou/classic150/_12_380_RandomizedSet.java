package com.dalq.learn.javacode.likou.classic150;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;

/**
 * @author daling.qdl
 * @date 2024/5/30 下午11:11
 */
public class _12_380_RandomizedSet {
    private Set<Integer> set;

    public boolean insert(int val) {
        return set.add(val);
    }

    public boolean remove(int val) {
        return set.remove(val);
    }

    public int getRandom() {
        List<Integer> list = new ArrayList<>(set);
        Random random = new Random();
        return list.get(random.nextInt(list.size()));
    }
}
