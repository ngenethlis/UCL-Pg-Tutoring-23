--examples in haskell  

-- writing functions 

add' :: Int -> Int -> Int
add' x y = x + y

sub' :: Int -> Int -> Int
sub' x y = x - y

-- notice no return statements

-- conditionals and pattern matching

add'' :: Int -> Int -> Int
add'' 0 y = y
add'' x y = 1 + add'' (x - 1) y

-- addOne :: [Int] -> [Int]
-- addOne xs = [x+1 | x<-xs]

-- addOne' :: [Int] -> [Int]
-- addOne' [] = []
-- addOne' (x:xs) = x+1 : addOne xs

-- addOne'' :: [Int] -> [Int]
-- addOne'' xs = map (+1) xs

getEven :: [Int] -> [Int]
getEven xs = filter (\x -> if x `mod` 3==0 then True else False) xs

len' :: [Char] -> Int
len' s = foldr (\char acc -> acc + 1) 0 s
--             