areFollowingPatterns <- function(strings, patterns) {
    return(identical(as.numeric(factor(strings, levels=strings)),as.numeric(factor(patterns, levels=patterns))))
}
