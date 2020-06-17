W, H = gets.split.map(&:to_i)
g = W.gcd(H)

if W / g == 4
  puts '4:3'
else
  puts '16:9'
end