N = gets.to_i

dist = Array.new(N){Array.new(N,0)}
X = Array.new(N,0)
Y = Array.new(N,0)
t = {}
N.times do |i|
  X[i], Y[i] = gets.split.map(&:to_i)
end

for i in 0..N-1 do
  for j in i+1..N-1 do
    d = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
    if !t[d]
      t[d] = []
    end
    t[d].push([i,j])
  end
end

puts t

t.each do |k, v|
  puts k
end