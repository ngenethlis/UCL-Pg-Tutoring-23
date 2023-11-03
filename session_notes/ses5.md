# Session 5
 
- Attendance
- Structs
- cwk and structs
- Sorting 


## Structs :

Good reference : https://www.geeksforgeeks.org/structures-c/

What is a struct?

- A struct is a user defined data type
- It can be used to group items of possibly different types into a single type
- the *Struct*  keyword is used to define a structure
- the items in the structure are called *members*
- the members can be accessed using the . *dot* operator or the -> *arrow* operator
- the members can be of any data type including other structs
- the members are stored in memory in the order they are declared
- the size of the struct is the sum of the sizes of its members
- the typedef keyword can be used to define a struct and a type in one statement
- A struct member can have the same name as the struct itself ( can you think of a structure that would use this? )


Syntax for declaring a struct :



```c

struct struct_name {
    data_type member1;
    data_type member2;
    ...
}
```
The above is also called a template


Struct variable declaration with structure template:
    
 ```c
struct struct_name {
    data_type member1;
    data_type member2;
    ...
} var1, var2, ...;
```

Struct variable declaration with structure template defined before hand:

```c
struct struct_name var1, var2, ...;
```

Accessing members of a struct:

consider the following struct:

```c
struct student {
    int id;
    char name[20];
    float percentage;
} s1

s1.id = 1;
s1.name = "John";
s1.percentage = 86.5;
```
We can't initialise members inside the struct declaration

```c
struct student {
    int id = 1; //  COMPILER ERROR:  cannot initialize members here
    char name[20] = "John"; //  COMPILER ERROR:  cannot initialize members here
    float percentage = 86.5; //  COMPILER ERROR:  cannot initialize members here
} s1
```

Why can't we initialise members inside the struct declaration?

No memory allocated for data type declaration so no memory allocated for it. 

### Initialisation of structs:

#### 3 ways
- Assingment operator
- Initialiser list
- Designated initialiser List

#### Assingment operator

```c
struct student s1;
s1.id = 1;
s1.name = "John";
s1.percentage = 86.5;
```

#### Initialiser list

```c
struct student s1 = {1, "John", 86.5};
```

#### Designated initialiser List

```c
struct student s1 = {.id = 1, .name = "John", .percentage = 86.5};

// general syntax
struct structure_name str = { .member1 = value1, .member2 = value2, .member3 = value3 };
```
This allows struct members to be initialised in any order

### typedef

- typedef keyword is used to define an alias for the already existing data type
- To use structs we have to use struct struct_name 
- typedef can be used to define a shorter name for the struct

Struct template with seperate declaration:


```c
struct student {
    int id;
    char name[20];
    float percentage;
} 

typedef struct student student1;
```

Struct template with variable declaration:

```c

typedef struct student {
    int id;
    char name[20];
    float percentage;
} student;



```



### Extra structs 

#### Nested structs

Embedding one struct inside another struct
```c
struct parent {
    int member1;
    struct member_str member2 {
        int member_str1;
        char member_str2;
        ...
    }
    ...
}

```

Seperate declaration of nested structs

```c
struct member_str {
    int member_str1;
    char member_str2;
    ...
}

struct parent {
    int member1;
    struct member_str member2;
    ...
}

```

Note : Declaration for a struct should always be present before its use/definition as structure member. i.e declare member then parent

Why would a struct have a member that is the same type as the struct itself?

```c
typedef struct LinkedListNode {
    int data;
    struct LinkedListNode *next;
};
```
Using the linked list example lets see how we can use pointers and structs

```c

LinkedListNode *head = NULL;


```

## CWK and structs 

Consider :
- What is the data we need to store?
- What is the best way to store it, access and modify it?

## Sorting

#### Intuition and Basic Sorting Algorithms


