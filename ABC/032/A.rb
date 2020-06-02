a = gets.to_i
b = gets.to_i
n = gets.to_i

l = a.lcm(b)
ans = l * (n / l)

if ans >= n
  puts ans
else
  puts ans + l
end
