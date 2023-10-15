# This week more C
-  Include 
-  Header files
-  Source files
-  Arrays
-  Intro to pointers if we have time

## Include and Preprocessor Directives
Some directives you might see:
`#include <someFile.h`
`#include "someFile.h`

-  `#include` is a preprocessor directive
-  It tells the compiler to include the contents of another file
-  The contents of the file are inserted into the source file
-  You can use functions and variables from the included file

### Whats the difference <> vs "" ?
-  `#include <someFile.h>` is used for system header files
-  `#include "someFile.h"` is used for user defined header files
- The compiler will look for system header files in the system directories
- The compiler will look for user defined header files in the current directory or in the directories specified with the `-I` flag

## Declare vs Define
-  Declaring a function or variable tells the compiler that it exists, what type it is, and what parameters it takes
-  Defining a function or variable tells the compiler what it is, what it does, and how it works



## Header Files
-  Header files are used to declare functions and variables
-  Header files are included in source files

### Example
```c
// someFile.h
int add(int a, int b);
```

```c
// main.c
#include <stdio.h>
#include "someFile.h"
int main(void) {
    int a = 5;
    int b = 10;
    int c = add(a, b);
    printf("%d + %d = %d\n", a, b, c);
    return 0;
}
```

but we still need to define the function in a source file


## Source Files
-  Source files are used to define functions and variables


```c
// someFile.c
int add(int a, int b) {
    return a + b;
}
```

```c
// main.c
#include <stdio.h>
#include "someFile.h"
int main(void) {
    int a = 5;
    int b = 10;
    int c = add(a, b);
    printf("%d + %d = %d\n", a, b, c);
    return 0;
}
```

## C Compilation , Source and Header Files
- Looking at above example, we have 3 files
- `main.c` is the source file
- `someFile.h` is the header file
- `someFile.c` is the source file
- We need to compile all 3 files to get an executable
- We can compile all 3 files at once

```bash
gcc main.c someFile.c -o main
```

### Summary
-  Header files are used to declare functions and variables
-  Source files are used to define functions and variables
-  Header files are included in source files with `#include`
-  you can find the above code in the `code` directory,     pull it and run it


