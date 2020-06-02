n, m = gets.split.map(&:to_i)

tyoushin = 6 * m
tanshin = 30 * n < 360 ? 30 * n :30 * n - 360
tanshin += 0.5 * m

ans = (tanshin - tyoushin).abs <= 180 ? (tanshin - tyoushin).abs : 360 - (tanshin - tyoushin).abs

puts ans