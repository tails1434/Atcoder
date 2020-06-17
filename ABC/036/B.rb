N = gets.to_i
S = N.times.map{gets.chomp}

N.times do |i|
  tmp = ''
  N.times do |j|
    tmp += S[N-j-1][i]
  end
  puts tmp
end