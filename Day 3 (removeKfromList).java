// Definition for singly-linked list:
// class ListNode<T> {
//   ListNode(T x) {
//     value = x;
//   }
//   T value;
//   ListNode<T> next;
// }
//

//note: this crashes via stack overflow for large lists
// reimplementation of Haskell algorithm, which doesn't work well in Java
ListNode<Integer> removeKFromList(ListNode<Integer> l, int k) {
    if (l==null)
        return null;
    if (l.value==k&&l.next!=null)
        return removeKFromList(l.next, k);
    if (l.value==k&&l.next==null)
        return null;
    ListNode<Integer> temp = new ListNode<Integer>(l.value);
    if (l.next==null)
        return temp;
    temp.next=removeKFromList(l.next, k);
    return temp;
}
