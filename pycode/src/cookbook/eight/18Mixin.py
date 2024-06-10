# 用Mixin技术来扩展类定义
# 对已有的类增加一些可能的功能特性
# super()

# 或者可以使用类装饰器：注解形式
# see 13DataModelOrTypeSystem.py

# 先定义一个Mixin类，里边的方法执行逻辑主要是super()的
# 然后再定义一个新类，继承自上文Mixin和需要扩展的类
# 执行新类的方法