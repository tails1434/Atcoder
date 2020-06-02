L, H = gets.split.map(&:to_i)
N = gets.to_i

N.times do
  a = gets.to_i
  if a < L
    puts L - a
  elsif a > H
    puts -1
  else
    puts 0
  end
end