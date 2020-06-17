N, K = gets.split.map(&:to_i)
W, P = N.times.map{gets.split.map(&:to_i)}.transpose

def check(x)
  tmp = []
  N.times do |i|
    tmp.push(W[i].to_f*(P[i].to_f - x.to_f))
  end
  tmp.sort!.reverse!
  value = 0.to_f
  K.times do |i|
    value += tmp[i]
  end
  return value >= 0
end

ok = 0.to_f
ng = 101.to_f
for i in 0..100
  mid = (ok + ng).quo(2).to_f
  if check(mid)
    ok = mid
  else
    ng = mid
  end
end

puts ok