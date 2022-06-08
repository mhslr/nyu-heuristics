```excel
B1 = A1 + 1
# now B1 depends on A1
# you cannot have A1's formula depend on B1
# reactivity: editing A1 will change B1
```
```cpp
int a = 1;	// declaration, allocates memory
a = 2;		// reassignment
int b = a;	// copies the memory content elsewhere
int& c = a;	// new reference/name, same memory location
c += 1;		// also increments a, b doen't change
```
```java
class MyClass {
  private String content;
  ...
  public MyClass(MyClass another) {
    this.content = another.content;
  }
}
MyClass a = new MyClass("hey");
MyClass b = a;  // points to same object as a
MyClass c = new MyClass(a); // calls copy contructor
b.setContent("you");  // modifies a, not c
```
```py
a = 1  # declaration/reassignment
b = a  # now b == 1
a = a + 1 # b doesn't change
# += is confusing, but does the same thing

c = []
d = c  # points to the same list object
e = c.copy()  # new list object
assert (c is d) and (c is not e)
c.append(1)  # will change d, not e
```
