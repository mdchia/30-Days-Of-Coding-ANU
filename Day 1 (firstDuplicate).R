firstDuplicate <- function(a) {
    idx<-anyDuplicated(a)

    if(idx>0){
        return(a[idx])
    } else {
        return(-1)
    }
}
