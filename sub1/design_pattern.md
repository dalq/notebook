## 1.sample factory（创建模式）
- Fruit apple = FruitFactory.newInstance("Apple");
- Fruit：是抽象产品类

## 2.Factory Method（创建模式）
- 抽象工厂、具体工厂、抽象产品、具体产品
- FruitFactory appleFac = new AppleFactory();
- Fruit apple = appleFac.newInstance();
- 比较：有新的产品添加到系统中时，工厂方法模式：就不需要修改核心的"工厂类"

## 3.Abstract Factory（创建模式）
- 抽象工厂、具体工厂、抽象产品1、具体产品1、抽象产品2、具体产品2、……
- 三星&苹果工厂生产的：手机、电脑

## 4.Simple Factory（创建模式）
- 确保类**只有一个实例**
- 123

## 5.Multiton
- 一个类有多个相同实例，而且该实例都是该类本身

## 6.建造模式
- 对象的“创建”和“标识”分割开
- Director, Builder, ConcreteBuilder, Product