## java中集合
- Collection
    + List
        * LinkedList, 
        * ArrayList, 
        * Vector, 
        * Stack
    + Set
        * HastSet
        * TreeSet
- Map
    + HashMap，
    + WeakHashMap, 
    + Hashtable
    + TreeMap

## j.u.c中集合
- [UML图](http://wangkuiwu.github.io/2012/08/14/juc-col01/)

###  List：CopyOnWriteArrayList
- 通过成员变量互斥锁lock实现了对CopyOnWriteArrayList的互斥访问
- 创建，都会调用setArray函数：
    + private transient volatile Object[] array:对于volatile的读取，总是可以看到所有线程对于他的最后的写入
- 添加：
    + 首先获取互斥锁
    + 操作完毕后，也是调用SetArray函数更新
- 读取：
- 删除：
    + 如果被删除的是最后一个元素，则直接setArray(Arrays.copyOf(elements, len - 1))
    + 否则新建数组，然后arrayCopy这个新数组，然后再setArray这个新数组
- 遍历：
    + COWIterator实现，不支持元素修改操作
- fail-fast：不会抛出fail-fast异常，但是arrayList会的！


### Set：CopyOnWriteArraySet、ConcurrentSkipListSet
#### CopyOnWriteArraySet
- HashSet是通过HashMap实现的，而CopyOnWriteArraySet是通过List：CopyOnWriteArrayList实现的
- 同上， 大小通常保持很小，只读操作远多于可变操作，需要在遍历期间防止线程间的冲突
- CopyOnWriteArrayList中的addIfAbsent()和addAllAbsent()方法，保证不会有重复元素

#### ConcurrentSkipListSet
- 通过ConcurrentSkipListMap实现

### Map：ConcurrentHashMap、ConcurrentSkipListMap
#### ConcurrentHashMap
- hashTable是通过synchronized来保证线程安全的
- HashTable是通过一把锁来控制，而ConcurrentHashMap是将哈细表分为许多片段，每个片段分别用一个互斥锁来控制并发
- jdk8开始，不用segment了，而是使用CAS
- 初始化：
    + 成员变量：
        * baseCount：
        * sizeCtl：-1正在初始化、-N有n个线程正在扩容？、正数：大于0是扩容的阈值，等于0是默认值
        * 节点类Node：val和next是volatile类型
        * TreeBin：与HashMap不同的点：它并不是直接转换为红黑树，而是把这些结点包装成TreeNode放在TreeBin对象中，由TreeBin完成对红黑树的包装，也就是说实际的ConcurrentHashMap数组中存放的元素不是TreeNode而是TreeBin
        * ForwardingNode：用于连接两个table的节点类
        * 对于指定节点操作的三个方法：tabAt、casTabAt、setTabAt：
    + 初始化时候是设置一些参数值而已，整个table的初始化是再插入元素时候发生的，例如put、computeIfAbsent、compute、merge 
        * 如果sizeCtl<0说明其他线程正在初始化，当前线程就放弃初始化
        * 否则将sizeCtl置为-1，说明本线程正在初始化table
- 扩容：transfer：TODO

#### ConcurrentSkipListMap
- 通过跳表实现的，而TreeMap是通过红黑树实现

### Queue：ArrayBlockingQueue, LinkedBlockingQueue, LinkedBlockingDeque, ConcurrentLinkedQueue和ConcurrentLinkedDeque
#### ArrayBlockingQueue
- 对标LinkedList
- **数组**实现、界限；FIFO
- 默认使用非公平锁
- 包含两个Condition对象(notEmpty和notFull)

#### LinkedBlockingQueue
- 对标LinkedList
- **单向链表**实现的阻塞队列
- FIFO
- 对于插入和取出采用不同的锁

#### LinkedBlockingDeque
- 双向链表实现的双向并发阻塞队列
- FIFO和FILO

#### ConcurrentLinkedQueue
- 链表
- FIFO
- 通过volatile实现多线程对于竞争资源的互斥访问

#### ConcurrentLinkedDeque