function climbingStairs($n) {
    $n+=1;
    $n0=0;
    $n1=1;
    $n2=$n0+$n1;
    if($n==1){
        return $n1;
    }
    if($n==2){
        return $n2;
    }
    for($x=1; $x<=$n; $x++){ // Iterative fibonacci sequence generator
        $n0=$n1;
        $n1=$n2;
        $n2=$n1+$n0;
    }
    return $n0;
}
