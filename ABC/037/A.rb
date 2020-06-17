A, B, C = gets.split.map(&:to_i)

ans = C / [A,B].min
ans += (C % [A,B].min) / [A,B].max
puts ans