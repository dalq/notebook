- 1、your-first0python-grogram
    - everything in Python is an object. Classes are objects. Class instances are objects. Even modules are objects.
    - Python uses try...except blocks to handle exceptions, and the raise statement to generate them. Java and c++ use try...catch blocks to handle exceptions, and the throw statement to generate them.
    - 直接命令行import module，module._name_是文件名；命令行运行py文件则其_name_是_main_

- 2、native-datatypes
    - 小数点后15位、shell中可以定义函数，每行回车，最后再空行回车作为结束
    - list
        - extend()入参为list，将list中每个元素接到后边；append（）入参为一个元素，如果输入为list则，后边将加一个 list元素！
        - a_list.count('new')、'new' in a_list 、a_list.index('mpilgrim') ：第一次出现的元素的index；没有的话使用index函数会抛异常！Good！否则后续会有更加难受的bug！
        - del a_list[1]删除元素  or  a_list.remore("new")a：删除第一个出现的！  fill the gap，lists never have gaps；同样如果删除一个没有的元素，也会抛异常
        - pop，删除最后一个元素，当然也可以指定index；pop空list会抛异常！
        - ``Empty lists are false; all other lists are true.``
    - tuples
        + immutable list
        + **list用 [] 来定义； 而tuples用（）来定义！**
        + 比list快；代码安全，不必考虑被改写  write-protect；被用作dictionary的keys？
        + tuple() freezes a list, and list() thaws a tuple.
        + 创建单个元素的tuples：需要加个逗号！  (False,)
        + (ONE, TWO) = range(2); >>> ONE   >>> 0； range函数返回 an iterator， 而不是list或者tuple
    - sets
        - **set用{}来定义**
        - a_set = set(a_list)
        - 创建空set：set()；**如果用{}定义出来的讲师一个空dictionary**：历史原因，坑？
        - 新增元素：2种：
            + add
            + update：任何入参类型：list、tuple等
        - 删除：3种：
            + discard：删除不存在的元素不会报错
            + remove：删除不存在的元素会报错
            + pop：随机的。。。,对空set进行pop操作会抛异常
            + a_set.clear()等价于a_set = set()
        - in； union：并集；intersection：交集；difference：a包含b不包含；**symmetric_difference：并集中去除交集的部分**
        - issubset、issuperset：相同元素，也算是子集&父集！
        - ``an empty set is false``
    - dictionaries
        - 类似于set的定义，但是KV之间用冒号隔开！
        - **读取没有的key会报错** a_dic['key'], a_dic['add_key'] = 'add_value'
        - SUFFIXES[1000][3]：1000这个key对应的list中的第四个元素
        - ``Empty dictionaries are false; all other dictionaries are true.``
    - none
        + None is False
        + not None is True
- 3、Comprehensions
    - 工作路径
        + import os; print(os.getcwd()); os.chdir('...'); 获取文件绝对路径：print(os.path.realpath('feed.xml'))
        + os.path.join()：不同OS有不同的斜线路径，所以用这个函数，let the python do the right thing！
        + os.path.expanduser(): 某个用户的主路径（home direction）
        + print(os.path.join(os.path.expanduser('~'), 'diveintopython3', 'examples', 'humansize.py'))：自动连接**各级目录**
        + (dirname, filename) = os.path.split(pathname) 返回的是tuple类型！
        + (shortname, extension) = os.path.splitext(filename) 返回文件名，和文件类型
        + ``The glob module uses shell-like wildcards.``通配符。import global；寻找某个路径下某些符合这个名的文件
        + metadata = os.stat('feed.xml')返回的对象是包含该文件信息的对象
        + import time：time.localtime(metadata.st_mtime);  import humansize：humansize.approximate_size(metadata.st_size)
    - LIST表达式？
        + list comprehension：[elem * 2 for elem in a_list] ；a_list = [elem * 2 for elem in a_list]这样也是可以的！new list在内存中构建
        + __[os.path.realpath(f) for f in glob.glob('*.xml')] 显示寻找到的这几个文件的绝对路径__
        + if 表达式：[f for f in glob.glob('*.py') if os.stat(f).st_size > 6000]：注意作用的是在current direction！  6000 bytes
        + [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.xml')] ：__构建了一个tuple__
        + [(humansize.approximate_size(os.stat(f).st_size), f) for f in glob.glob('*.xml')]
    - Dictionary表达式？ 
- 4、String
- 
         