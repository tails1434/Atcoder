S = gets.chomp
T = gets.to_i

len_S = S.size
cnt = 0
x = 0
y = 0
len_S.times do |i|
  if S[i] == 'L'
    x -= 1
  elsif S[i] == 'R'
    x += 1
  elsif S[i] == 'U'
    y += 1
  elsif S[i] == 'D'
    y -= 1
  else
    cnt += 1
  end
end

if T == 1
  puts x.abs + y.abs + cnt
else
  cnt.times do
    if x.abs >= y.abs
      if x >= 0
        x -= 1
      else
        x += 1
      end
    else
      if y >= 0
        y -= 1
      else
        y += 1
      end
    end
  end
  puts x.abs + y.abs
end