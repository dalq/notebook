 ## 锁
- 锁分为两类：同步锁（synchronized关键字），juc包中的锁
- j.u.c中的锁：
    - 独占锁：ReentrantLock
    - 共享锁：CountDownLatch, CyclicBarrier, Semaphore, ReentrantReadWriteLock
- sync 继承自 AQS

## j.u.c
### 互斥锁ReentrantLock
- 可重入的互斥锁
- 公平锁
- 非公平锁

#### 公平锁
- lock()函数，对于公平锁的获取过程
```java 
    final void lock() {
    acquire(1);
    }

    public final void acquire(int arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}
//(01) 先是通过tryAcquire()尝试获取锁。获取成功的话，直接返回；尝试失败的话，再通过acquireQueued()获取锁。
//(02) 尝试失败的情况下，会先通过addWaiter()来将“当前线程”加入到"CLH队列"末尾；然后调用acquireQueued()，在CLH队列中排序等待获取锁，在此过程中，线程处于休眠状态。直到获取锁了才返回。 如果在休眠等待过程中被中断过，则调用selfInterrupt()来自己产生一个中断。
```

- tryAcquire：让当前线程尝试获取锁，获取成功则返回true，否则返回false
    + 如果一个字段被声明成volatile，java线程内存模型确保所有线程看到这个变量的值是一致的。
- addWaiter：将当前线程添加到CLH队列中。这就意味着将当前线程添加到等待获取“锁”的等待线程队列中了
    + 对于“公平锁”而言，addWaiter(Node.EXCLUSIVE)会首先创建一个Node节点，节点的类型是“独占锁”(Node.EXCLUSIVE)类型。然后，再将该节点添加到CLH队列的末尾
- acquireQueued：逐步执行CLH队列中的线程
- selfInterrupt：当前线程自己产生一个中断

- unlock()函数，对于公平锁的释放过程
    + 释放锁时，主要进行的操作，是更新当前线程对应的锁的状态。如果当前线程对锁已经彻底释放，则设置“锁”的持有线程为null，设置当前线程的状态为空，然后唤醒后继线程。

#### 非公平锁
- 公平锁和非公平锁的区别，是在获取锁的机制上的区别。表现在，在尝试获取锁时 —— 公平锁，只有在当前线程是CLH等待队列的表头时，才获取锁；而非公平锁，只要当前锁处于空闲状态，则直接获取锁，而不管CLH等待队列中的顺序。
只有当非公平锁尝试获取锁失败的时候，它才会像公平锁一样，进入CLH等待队列排序等待。

#### condition
- 同Object.wait()、Object.notify()和Object.notifyAll()对应功能一致，Object的方法用于synchronized同步块中，而Condition的方法用于ReentrantLock的lock(与unlock()之间。
- 能够更加精细的控制多线程的休眠与唤醒；通过notifyAll唤醒所有线程(但是notifyAll无法区分唤醒的线程是读线程，还是写线程)。 但是，通过Condition，就能明确的指定唤醒读线程


#### LockSupport

#### ReentrantReadWriteLock
- ReadWriteLock：维护了一对锁，读取锁：共享锁；写入锁：独占锁
- [源码](http://wangkuiwu.github.io/2012/08/13/juc-lock08/)

#### CountDownLatch
- 允许1或N个线程等待其他线程完成执行
- 通过共享锁实现，[例子](http://wangkuiwu.github.io/2012/08/13/juc-lock09/)
- "主线程"等待"5个子线程"全部都完成"指定的工作"之后，再继续运行

#### CyclicBarrier
- 允许一组线程互相等待，直到到达某个公共屏障点
- [新建5个线程，当这5个线程达到一定的条件时，执行某项任务。](http://wangkuiwu.github.io/2012/08/13/juc-lock10/)

#### Semaphore
- 计数信号量，本质是一个"共享锁"
- 根据共享锁的获取原则，分为公平信号量、以及非公平信号量
- 某个信号量的许可为10，线程1请求5是可以的，线程2请求4也是可以的，线程3请求7的时候这时只剩1了所以需要等待前两个线程释放了他们所持有的信号量许可后，才能获得7个许可
