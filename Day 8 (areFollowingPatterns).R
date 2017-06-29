areFollowingPatterns <- function(strings, patterns) {
    return(identical(as.numeric(factor(strings, levels=strings)),as.numeric(factor(patterns, levels=patterns))))
}
# The R factor data type associates an int with another value (usually strings)
# and is used to compress/validate categorical data (e.g. small/medium/large).
# Casting it to numeric reveals the underlying integers, and levels=strings
# ensures it is ordered by appearance (default is alphabetic). R == returns a
# bool for each list item, so identical() returns a single value comparing the
# lists as a whole.
