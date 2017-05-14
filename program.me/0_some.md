### sql
- on:
- 比如下边，where里的过率条件转为on里是不行的！
```sql
SELECT COUNT(*)
FROM A a
LEFT OUTER JOIN B b
ON a.admin_mbr_seq = b.admin_mbr_seq
    AND a.ds = 20170410
WHERE b.admin_mbr_seq IS NULL
```

### 1-log
#### 1.1-jcl框架
###### 1.1.1-log4j
- jcl §§§ log4j

#### 1.2-slf4j框架
###### 1.2.1-logback
- jcl-overlog4j、slf4j12-api、§§§ logback-classic、 log4j(可选)

###### 1.2.2-log4j
- log4j：**Log4j需要一个适配器slf4j-log4j12才能被SLF4J识别并使用**:jcl-overlog4j、slf4j12-api、§§§ log4j、slf4j-log4j12
- logback：
- 同时并存两者：pom.xml中，同时包含log4j和logback-classic这两个依赖，但是请一定不要包含 **slf4j-log4j12这个包，因为它会和logback-classic起冲突**

###### 1.2.3为什么要用桥接的包jcl-overlog4j呢
- 我理解的应用的依赖的二方库有不少其日志工具用的是jcl，所以slf4j推荐了这种桥接的方式

#### 1.2-转换
- log4j -> slf4j -> logback
- log4j-over-slf4j 先转为slf4j
- 使用slf4j+log4j的dependency： 1.slf4j-api （slf4j接口）； 2.slf4j-log4j (log4j 服务于slf4j的”驱动”)； 3.log4j (log4j 日志实现)；
- 使用slf4j+logback的dependency： 1.slf4j-api （slf4j接口）； 2.logback-classic (logback服务于slf4j的”驱动”)； 3.logback-core (logback日志实现)； 4.log4j-over-slf4j(如果系统有依赖log4j日志体系，想统一对接到logback，则需要依赖此包)；