A, D = gets.split.map(&:to_i)

attack = (A + 1) * D
defence = A * (D + 1)

if attack >= defence
  puts attack
else
  puts defence
end