## Thread Runnable
- Runnable还可以用于“资源的共享”。即，多个线程都是基于某一个Runnable对象建立的，它们会共享Runnable对象上的资源。

## synchronized
- static synchronized 可以看作是类锁，普通synchronized可以看作是对象锁，只针对**这个对象的锁**(ref)[http://wangkuiwu.github.io/2012/08/04/threads-basic/]
