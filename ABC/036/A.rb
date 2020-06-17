A, B = gets.split.map(&:to_i)

if B % A == 0
  puts B / A
else
  puts B / A + 1
end