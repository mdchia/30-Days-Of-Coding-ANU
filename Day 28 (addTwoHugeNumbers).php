// Definition for singly-linked list:
// class ListNode {
//   public $value;
//   public $next;
//
//   public function __construct($x) {
//     $this->value = $x;
//     $this->next = null;
//   }
// }
//

function linkedListToStr($ll){
    $a_str="";
    if($ll==null){
        return $a_str;
    }
    while ($ll != null){
        if($a_str==""&&$ll->value==0){ // strip leading zeros
            $ll=$ll->next;
            continue;
        }
        $raw=(string) $ll->value;
        while(strlen($raw)!=4){ // pad in leading zeros
            $raw='0'.$raw;
        }
        $a_str.=$raw;
        $ll=$ll->next;
    }
    return $a_str;
}
function addTwoHugeNumbers($a, $b) {
    $a_str=linkedListToStr($a);
    $b_str=linkedListToStr($b);
    $carry=0;
    $c_str="";
    #print($b_str."\n".$a_str."\n");
    $min_str=min(strlen($a_str),strlen($b_str));
    $diff=abs(strlen($a_str)-strlen($b_str));
    if($min_str==0&&$diff==0){
        return [0];
    }
    for ($i=1;$i<$min_str+1;$i++){
        $c1=$a_str[-$i];
        $c2=$b_str[-$i];
        $c3=$c1+$c2+$carry;
        $carry=0;
        if($c3>9){
            $carry=1;
            $c3-=10;
        }
        $c_str=$c3.$c_str;
        #print($c1.",".$c2.",".$c3.",".$i.','.$carry.','.$c_str."\n");
    }
    if ($carry!=0){
        for ($i=$min_str+1;$i<$min_str+$diff+1;$i++){
            if(strlen($a_str)>strlen($b_str)){
                $c1=$a_str[-$i];
            } elseif(strlen($a_str)<strlen($b_str)) {
                $c1=$b_str[-$i];
            } else {
                $c_str='1'.$c_str;
                break;
            }
            $c3=$c1+$carry;
            $carry=0;
            if($c3>9){
                $carry=1;
                $c3-=10;
            }
            $c_str=$c3.$c_str;
            #print($c1.",".$c3.",".$i.','.$carry.','.$c_str."\n");
        }
        if ($carry!=0){
            $c_str='1'.$c_str;
        }
    }
    elseif ($diff!=0){
        if (strlen($a_str)>strlen($b_str)){
            $head=substr($a_str,0,$diff);
        } else {
            $head=substr($b_str,0,$diff);
        }
        $c_str=$head.$c_str;
    }
    while(strlen($c_str)%4!=0){
        $c_str='0'.$c_str;
        #print($c_str."\n");
    }
    $c_arr=array_map('intval', str_split($c_str,4));
    return $c_arr;
}
