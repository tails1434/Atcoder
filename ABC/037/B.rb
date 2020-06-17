N, Q = gets.split.map(&:to_i)
ans = Array.new(N,0)

Q.times do
  l, r, t = gets.split.map(&:to_i)
  l -= 1
  r -= 1
  for i in (l..r) do
    ans[i] = t
  end
end

puts ans