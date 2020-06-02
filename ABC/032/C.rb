N, K = gets.split.map(&:to_i)
s = N.times.map {gets.to_i}

if s.include?(0)
  puts N
  exit
end

ans = 0
tmp = 1
right = 0
(0..N-1).each do |left|
  while right - left >= 0 and right < N
    if tmp * s[right] <= K
      tmp *= s[right]
      ans = [right - left + 1, ans].max
      right += 1
    else
      break
    end
  end
  tmp /= s[left]
end

puts ans