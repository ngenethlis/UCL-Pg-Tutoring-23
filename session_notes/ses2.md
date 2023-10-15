# This week C

- Data types
- Control flow (if, for, while)
- Functions



# Data types

## Basic types

- char
- int
- float
- double
- long 
- short
- and their unsigned versions

- void (no type, more on later sessions)

# Control flow

## if

```c
if (condition) {
    // do something
} else if (condition) {
    // do something else
} else {
    // do something else
}
```

## switch

```c
switch (expression) {
    case constant1:
        // do something
        break;
    case constant2:
        // do something
        break;
    default:
        // do something
        break;
}
```

## for

```c
for (initialization; condition; increment) {
    // do something
}
```

## while

```c

while (condition) {
    // do something
}
```

## do while 

```c

do {
    // do something
} while (condition);
```

## Notice
- While loop is a pre-test loop.
- Do while loop is a post-test loop.
- Which means :
 - while loop checks the condition  before executing the loop body and the do while loop checks the condition after executing the loop body.
- Do While loop executes the loop body at least once.
- semicolon at the end of the do while statement.


# Functions

## Function declaration

```c
return_type function_name (type1 parameter1, type2 parameter2, ...) {

    statement1;
    statement2;
    ...
    // do something
    return statement;
}
```

## Function call

```c
return_type func(type1 arg1, type2 arg2, ...){
    //do something
    // call function
    function_name (argument1, argument2, ...);
    // or assign return value to a variable
    variable = function_name (argument1, argument2, ...);
    // or use return value directly
    return function_name (argument1, argument2, ...);
    // or just return
    return statement;
}
```