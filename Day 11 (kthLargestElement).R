kthLargestElement <- function(nums, k) {
    numList<-sort(as.numeric(nums),decreasing=TRUE)
    return(numList[k])
}
