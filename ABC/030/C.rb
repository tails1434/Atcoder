N, M = gets.split.map(&:to_i)
X, Y = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
B = gets.split.map(&:to_i)
cnt = 0
time = A[0]
ans = 0
while true
  if cnt % 2 == 0
    time = B.bsearch{|x| x >= time + X}
    if !time
      break
    end
  else
    ans += 1
    time = A.bsearch{|x| x >= time + Y}
    if !time
       break
    end
  end
  cnt += 1
end

puts ans