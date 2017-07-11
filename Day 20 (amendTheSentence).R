amendTheSentence <- function(s) {
    final <- ""
    for (i in 1:nchar(s)){
        c <- substring(s, i, i)
        if(c == toupper(c)){
            if(i==1){
                final <- tolower(c)
            } else {
                final <- paste(final, tolower(c))
            }
        } else {
            final <- paste(final,c,sep="")
        }
    }
    return(final)
}
