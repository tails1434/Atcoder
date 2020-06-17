N, K = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
B = Array.new(N+1,0)

N.times do |i|
  B[i+1] = A[i] + B[i]
end

ans = 0

(N-K+1).times do |i|
  ans += B[i+K] - B[i]
end

puts ans