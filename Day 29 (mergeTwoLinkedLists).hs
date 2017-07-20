-- Definition for singly-linked list:
-- data ListNode a = ListNode { val :: a
--                            , next :: ListNode a
--                            } | Nil deriving Show
--

mergeTwoLinkedLists :: Ord a => ListNode a -> ListNode a -> ListNode a

mergeTwoLinkedLists Nil Nil = Nil

mergeTwoLinkedLists (ListNode v1 n1) Nil = (ListNode v1 n1)

mergeTwoLinkedLists Nil (ListNode v2 n2) = (ListNode v2 n2)

mergeTwoLinkedLists (ListNode v1 n1) (ListNode v2 n2)
    | v1 > v2 = ListNode v2 (mergeTwoLinkedLists (ListNode v1 n1) n2)
    | v1 < v2 = ListNode v1 (mergeTwoLinkedLists (ListNode v2 n2) n1)
    | otherwise = ListNode v1 (mergeTwoLinkedLists (ListNode v2 n2) n1)
