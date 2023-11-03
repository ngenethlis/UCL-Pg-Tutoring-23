# This week :
- attendance
- pointers 
- debugging in VSC 
- signed vs unsigned


## First : Pointers

### Before dealing with pointers, whats a value?
```c
int x = 145;
```
- x is a variable
- 145 is a value
- x is a variable that holds a value

suppose we have a function that takes a variable and adds 1 to it
```c
void addOne(int x){
    x++;
    printf("%d\n", x);
}
```
used like this:
```c    
int main(){
    int x = 145;
    addOne(x);
    printf("%d\n", x);
    return 0;
}
```
what will main print?

the function addOne gets x, adds one to it and prints it. it doesn't change the value of x in main.

what if we used pointers?

```c
void addOne(int *x){
    (*x)++;
    printf("%d\n", *x);
}
```
used like this:
```c
int main(){
    int *x = &145;
    addOne(x);
    printf("%d\n", x);
    return 0;
}
```
what will main print?
why?

### Pointers
- a pointer is a variable that holds a memory address
- a pointer can point to a variable
- a pointer can point to another pointer
- a pointer can point to a function
- a pointer can point to an array

### How to declare a pointer to store a value of type int
```c
int *p;
```
if we want p to store a value 5
```c
int *p;
int x = 5;
p = &x;
printf("%d\n", *p);
```

- &x is the address of x
- so p is a pointer that points to x

## how is * and & used in pointers?
- & is used to get the address of a variable
- \* is used to get the value of the memory address that a pointer points to



# Arrays, pointers in disguise

- arrays use special syntax ``[]`` to access elements
- ``[]`` is just syntactic sugar for pointer arithmetic
- ``a[i]`` is the same as ``*(a+i)``

```c
int a[5] = {1,2,3,4,5};
for (int i = 0; i < 5; i++){
    printf("%d\n", a[i]);
}
```
is the same as
```c
int a[5] = {1,2,3,4,5};
int *p = a;
for (int i = 0; i < 5; i++){
    printf("%d\n", *(p+i));
}
```

### Char arrays and strings

- strings are char arrays
- strings are null terminated with \0

```c
char hello[6] = {'h', 'e', 'l', 'l', 'o', '\0'};
char hello2[6] = "hello";
char *hello3 = "hello";
```

- All 3 are the same thing just different syntax



### Extra: why do we use & for scanf?
```c
int x;
scanf("%d", &x);

```
scanf takes the location of x, so it can change the value stored there


## Second : Debugging C in VSC
Setup:
- install C/C++ extension
- install gcc
- install gdb
- use vsc to setup a launch.json file 
- include program path in the launch.json file
- if you are getting miDebugger path errors include the path to gdb in the launch.json file
- use the debugger to run the program




## Third : Signed vs Unsigned
- signed numbers can be positive or negative
- unsigned numbers can only be positives
- size : signed and unsigned are the same size
- signed numbers use the first bit to store the sign
- unsigned numbers use all bits to store the value

```c
int x = 5;
unsigned int y = 5;
```
Why do we have unsigned numbers?
- unsigned numbers can store larger values because they don't have to store the sign bit
- so if we know we only want to deal with positive numbers, we can use unsigned to store larger valuess

```c
int x = -1;
unsigned int y = -1;
```
what will x and y store?

- x will store -1
- y will store 4294967295 (2^32 - 1)
- as we decrease y, it will go from 4294967295 to 0

```c
unsigned int y = -1;
y--;
printf("%u\n", y);
printf("%d\n", y);
```
what will this print?


