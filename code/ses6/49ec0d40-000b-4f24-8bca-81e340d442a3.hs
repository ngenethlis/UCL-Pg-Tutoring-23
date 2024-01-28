# examples in haskell  

# writing functions 

add' :: Int -> Int -> Int
add' x y = x + y

sub' :: Int -> Int -> Int
sub' x y = x - y

# notice no return statements

# conditionals and pattern matching

add'' :: Int -> Int -> Int
add'' 0 y = y
add'' x y = 1 + add (x - 1) y


