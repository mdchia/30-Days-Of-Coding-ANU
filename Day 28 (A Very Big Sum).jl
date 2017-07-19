x = parse(Int, readline(STDIN))
y = readline(STDIN)
y = split(y)
a = 0

for i in 1:x
    a+=floor(parse(Int, y[i]))
end


println(a)
