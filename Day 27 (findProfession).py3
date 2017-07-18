def findProfession(level, pos):
    def thue_morse(n): # https://stackoverflow.com/a/36507150
        return bin(n).count("1") % 2
    pos = (pos-1) % (1 << level-1) + 1
    if thue_morse(pos-1):
        return "Doctor"
    else:
        return "Engineer"
