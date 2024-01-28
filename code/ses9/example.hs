
min' :: [Int] -> Int
min' [x] = x
min' (x:xs) = if x > min' xs then min' xs else x

minF :: [Int] -> Int
minF [x] = x
minF xs = foldr1 (\x acc -> min x acc) xs


listOfVals :: (Int -> Int) -> Int -> [Int]
listOfVals f n = map f [0..n]


minVal:: (Int -> Int) -> Int -> Int
minVal f n = minF (listOfVals f n)

equalVals :: (Int -> Int) -> Int -> Bool
equalVals f n = foldr (\x acc-> x==(f 0) && acc) True (listOfVals f n)

greaterThanZero ::(Int->Int)->Int ->Bool
greaterThanZero f n = foldr (\x acc-> x > 0 && acc) True (listOfVals f n)

increasing ::(Int->Int)->Int ->Bool
increasing f 0 = True
increasing f n = if f n > f (n-1) then increasing f (n-1) else False