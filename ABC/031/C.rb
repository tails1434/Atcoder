N = gets.to_i
a = gets.split.map(&:to_i)

ans = -10 ** 5
(0..N-1).each do |i|
  aoki = []
  (0..N-1).each do |j|
    if i == j
      next
    end
    left = [i,j].min
    right = [i,j].max
    t = a.[](left..right)
    even = t.select.with_index { |_, i| i.odd? }
    aoki.push(even.inject(:+) )
  end
  j = aoki.index(aoki.max)
  left = [i,j].min
  right = [i,j].max
  t = a.[](left..right)
  odd = t.select.with_index { |_, i| i.even? }
  ans = [ans,odd.inject(:+)].max
end

puts ans