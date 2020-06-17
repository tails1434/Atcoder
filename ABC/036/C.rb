require 'set'

N = gets.to_i
a = N.times.map{gets.to_i}
s = Set.new

N.times do |i|
  s.add(a[i])
end

b = s.to_a
b.sort!
d = {}
b.size.times do |i|
  d[b[i]] = i
end
N.times do |i|
  puts d[a[i]]
end