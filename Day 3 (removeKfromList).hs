-- Definition for singly-linked list:
-- data ListNode a = ListNode { val :: a
--                            , next :: ListNode a
--                            } | Nil deriving Show
--
removeKFromList :: Eq a => ListNode a -> a -> ListNode a
removeKFromList (ListNode val next) k
    |val == k = removeKFromList next k -- if the value is the same, move on without including it
    |otherwise = (ListNode val (removeKFromList next k)) -- otherwise return the same thing but recursively checking the next item
removeKFromList Nil k = Nil
