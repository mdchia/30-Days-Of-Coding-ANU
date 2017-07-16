function printEven(s)
    print(s[1:2:end])
    print(" ")
    print(s[2:2:end])
    print('\n')
end

x = parse(Int, readline(STDIN))
for i=1:x
    printEven(strip(readline(STDIN)))
end
