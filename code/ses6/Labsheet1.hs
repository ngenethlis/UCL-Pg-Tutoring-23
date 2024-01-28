
min :: [Int] -> Int
min [x] = x
min (x:xs) = if x > min xs then min xs else x
