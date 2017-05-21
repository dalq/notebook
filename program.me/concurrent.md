## 线程的状态
- new - runnable - blocked(wait, lock, sleep join等) - running - dead

## 线程实现的几种方式(ref)[http://www.cnblogs.com/hanganglin/p/3517178.html]
- 继承Thread类：多线程之间无法共享资源
- 实现Runnable接口（推荐）：多个线程之间需要处理共享资源的时候
- FutureTask
- TimerTask

## Thread类
- Runnable还可以用于“资源的共享”。即，多个线程都是基于某一个Runnable对象建立的，它们会共享Runnable对象上的资源。
- start()：新起一个线程，新线程会执行run方法
- run()：和普通的成员函数一样，可以被重复调用

## synchronized
- 实例锁与对象锁：static synchronized 可以看作是类锁，普通synchronized可以看作是对象锁，只针对**这个对象的锁**(ref)[http://wangkuiwu.github.io/2012/08/04/threads-basic/]
- 基本原则：线程A访问对象a的synchronized方法或者代码块，线程B都于**所有**同步的方法或者代码块的访问都将被阻塞，但是对于对象a的非同步代码块是可以访问的

## wait()、notify()
- (t1.wait()应该是让“线程t1”等待；但是，为什么却是让“主线程main”等待了呢？)[http://wangkuiwu.github.io/2012/08/05/threads-basic/]
- Object.wait()、Object.notify()和Object.notifyAll()方法必须在synchronized同步块内使用

## yield()
- wait()是让线程由“运行状态”进入到“等待(阻塞)状态”，而yield()是让线程由“运行状态”进入到“就绪状态”。
- wait()是会线程释放它所持有对象的同步锁，而yield()方法不会释放锁。

## sleep()

