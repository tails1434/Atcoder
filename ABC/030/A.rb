A, B, C, D = gets.split.map(&:to_i)

if B / A.to_f > D / C.to_f
  puts 'TAKAHASHI'
elsif B / A.to_f < D / C.to_f
  puts 'AOKI'
else
  puts 'DRAW'
end