# Function函数式接口

Java8提供了函数式接口，配合Lambda表达式使用，可以简化代码

使用`@FunctionalInterface`标识接口，并且该接口只包含一个**抽象**方法（可以有多个非抽象方法），否则IDE会提示错误。主要分为几类

1. Supplier供给型函数：只有返回值

```java
@FunctionalInterface
public interface Supplier<T> {
    T get();
}
```

2. Consumer消费型函数：只接收参数

```java
@FunctionalInterface
public interface Consumer<T> {
    void accept(T t);
    //多个Consumer处理参数
    default Consumer<T> andThen(Consumer<? super T> after) {
        Objects.requireNonNull(after);
        return (T t) -> { accept(t); after.accept(t); };
    }
}
```

3. Runable无参无返回值

```java
@FunctionalInterface
public interface Runnable {
    public abstract void run();
}
```
4. Function既有参数又有返回值

```java
@FunctionalInterface
public interface Function<T, R> {
    R apply(T t);
    //组合函数，先执行传入的函数，再执行自身
    default <V> Function<V, R> compose(Function<? super V, ? extends T> before) {
        Objects.requireNonNull(before);
        return (V v) -> apply(before.apply(v));
    }
    //组合函数，先执行自身，再执行传入的函数
    default <V> Function<T, V> andThen(Function<? super R, ? extends V> after) {
        Objects.requireNonNull(after);
        return (T t) -> after.apply(apply(t));
    }

    static <T> Function<T, T> identity() {
        return t -> t;
    }
}
```
5. Predicate接收参数返回布尔值，一般用于验证参数是否满足要求

```java
@FunctionalInterface
public interface Predicate<T> {
    boolean test(T t);
    //且
    default Predicate<T> and(Predicate<? super T> other) {
        Objects.requireNonNull(other);
        return (t) -> test(t) && other.test(t);
    }
    //非
    default Predicate<T> negate() {
        return (t) -> !test(t);
    }
    //或
    default Predicate<T> or(Predicate<? super T> other) {
        Objects.requireNonNull(other);
        return (t) -> test(t) || other.test(t);
    }

    static <T> Predicate<T> isEqual(Object targetRef) {
        return (null == targetRef)
                ? Objects::isNull
                : object -> targetRef.equals(object);
    }
}
```

6. BiFunction接收两个参数，有返回值

```java
@FunctionalInterface
public interface BiFunction<T, U, R> {
    R apply(T t, U u);

    default <V> BiFunction<T, U, V> andThen(Function<? super R, ? extends V> after) {
        Objects.requireNonNull(after);
        return (T t, U u) -> after.apply(apply(t, u));
    }
}
```

Java预置了一些函数式接口具体实现，基本都是脱胎于上述几种类型。

## 自定义函数接口消除`if...else`逻辑

```java
//1. 定义函数式接口
@FunctionalInterface
public interface BranchHandler() {
  void trueOrFalseHandle(Runnable trueHandler, Runnable falseHandler);
}
//2. 编写判断逻辑
public static BranchHandler isTrueOrFalse(boolean flag) {
  return (trueHandler, falseHandler) -> {
    if(flag) {
      trueHandler.run();
    } else {
      falseHandler.run();
    }
  }
}
//3. 使用方式
@Test
void test() {
  //原始写法
  if (true) {
    doSomething();
  } else {
    doOther();
  }
  //使用函数式接口写法
  isTrueOrFalse(true).trueOfFalseHandler(() -> {
    doSometing();
  }, () -> {
    doOther();
  });
}
```





