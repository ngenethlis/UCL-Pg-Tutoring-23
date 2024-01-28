-- basic sorting algorithms



selectionSort :: (Ord a) => [a] -> [a]
selectionSort [] = []
selectionSort xs = let x = minimum xs
                   in x : selectionSort (remove x xs)
    where remove x xs = [y | y <- xs, y /= x]
-- 

insertionSort :: (Ord a) => [a] -> [a]
insertionSort [] = []
insertionSort (x:xs) = insert x (insertionSort xs)
    where insert x [] = [x]
          insert x (y:ys) = if x < y then (x : y : ys) else y : insert x ys
        -- insert x in sorted y:ys\
        

        
bubbleSort :: (Ord a) => [a] -> [a]
bubbleSort [] = []
bubbleSort xs = let (y, ys) = bubble xs
                in y : bubbleSort ys
    where bubble [x] = (x, [])
          bubble (x:y:xs) = if x > y then (y, x:xs) else (x, y:xs)

-- More complicated ones:

-- Merge sort 

-- fisrt merging two sorted lists
merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) | x <= y  = x : merge xs (y:ys)
                    | otherwise = y : merge (x:xs) ys

mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs  = merge sortedLeft sortedRight 
    where sortedLeft  = mergeSort left
          sortedRight = mergeSort right
          (left, right) = splitAt (length xs `div` 2) xs


-- Quick sort
quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x : xs) = quickSort left ++ [x] ++ quickSort right
    where   left  = [a | a <- xs, a < x]
            right = [a | a <-  xs, a >= x]



--  ys = [4,5,6] xs= [1,2,3]
--  3:ys = acc
-- 2:acc
-- 1:acc 
-- xs ++ ys