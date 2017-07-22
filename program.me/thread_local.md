- ThreadPoolExecutor
    + workers：HaseSet：通过他实现了一个线程集合
    + workQueue：BlockingQueue：通过他实现了阻塞功能
    + mainLock：ReentrantLock：通过他实现了对线程池的互斥访问
    + corePoolSize：核心池大小
    + maximumPoolSize：最大池大小
    + poolSize：当前线程池的实际大小
    + allowCoreThreadTimeOut和keepAliveTime：线程在空闲状态是否可以存货
    + threadFactory：线程池通过ThreadFactory创建线程
    + handler：某任务添加到线程池中，而线程池拒绝该任务时，线程池会通过handler进行相应的处理
- 状态：running-shutdown/stop-tidying-terminated
- 拒绝策略：AbortPolicy（默认、直接抛异常）, CallerRunsPolicy（被拒绝的任务添加到"线程池正在运行的线程"中取运行）, DiscardOldestPolicy（放弃队列中最旧的任务，然后件被拒绝的任务添加到队列中去）和DiscardPolicy（丢弃被拒绝的任务）