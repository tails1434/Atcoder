N, Q = gets.split.map(&:to_i)

imos = Array.new(N+1,0)

Q.times do
  l, r = gets.split.map(&:to_i)
  l -= 1
  imos[l] += 1
  imos[r] -= 1
end

ans = []
N.times do |i|
  if i != 0
    imos[i] += imos[i-1]
  end
  if imos[i] % 2 == 0
    ans.push('0')
  else
    ans.push('1')
  end
end

puts ans.join