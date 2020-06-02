require 'set'

s = gets.chomp
k = gets.to_i

if s.length < k
  puts 0
  exit
end

ans = Set.new
(0..s.length-k).each do |i|
  ans.add(s.slice(i,k))
end

puts ans.length