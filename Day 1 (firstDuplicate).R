firstDuplicate <- function(a) {
    idx<-anyDuplicated(a) # Returns index of the first duplicate, if it exists
    if(idx>0){
        return(a[idx])
    } else {
        return(-1)
    }
}
