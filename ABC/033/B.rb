N = gets.to_i
town = {}

total = 0
N.times do
  s, i = gets.split
  i = i.to_i
  town[s] = i
  total += i
end

town.each do |k, v|
  if v * 2 > total
    puts k
    exit
  end
end

puts 'atcoder'