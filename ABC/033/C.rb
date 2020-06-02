S = gets.chomp

cnt = 0
zero_flag = false
len = S.length - 1
S.each_char.with_index do |s, i|
  if s == '0'
    zero_flag = true
  end

  if s == '+'
    if !zero_flag
      cnt += 1
    end
    zero_flag = false
  end

  if i == len
    if !zero_flag
      cnt += 1
    end
  end
end

puts cnt