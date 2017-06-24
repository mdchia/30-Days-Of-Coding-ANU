-- Definition for singly-linked list:
-- data ListNode a = ListNode { val :: a
--                            , next :: ListNode a
--                            } | Nil deriving Show
--
removeKFromList :: Eq a => ListNode a -> a -> ListNode a
removeKFromList (ListNode val next) k
    |val == k = removeKFromList next k
    |otherwise = (ListNode val (removeKFromList next k))
removeKFromList Nil k = Nil
