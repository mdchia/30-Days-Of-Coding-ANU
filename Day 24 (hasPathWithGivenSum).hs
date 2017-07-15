--
-- Definition for binary tree:
-- data Tree a = Tree { value :: a
--                    , left :: Tree a
--                    , right :: Tree a
--                    } | Null deriving Show

hasPathWithGivenSum :: Integral a => Tree a -> a -> Bool
hasPathWithGivenSum Null 0 = True
hasPathWithGivenSum Null s = False
hasPathWithGivenSum (Tree val Null Null) s
    | val==s = True
hasPathWithGivenSum (Tree val l r) s
--    | val==s = True
    | otherwise = (checkPathSum l s val) || (checkPathSum r s val)

checkPathSum :: Integral a => Tree a -> a -> a -> Bool
checkPathSum Null _ _ = False
checkPathSum (Tree val Null Null) s run
    | (val+run) == s = True
    | otherwise = False
checkPathSum (Tree val l r) s run
--    | (val+run) == s = True
    | otherwise = (checkPathSum l s (val+run)) || (checkPathSum r s (val+run))
