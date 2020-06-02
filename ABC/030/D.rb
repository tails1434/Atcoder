n, a = gets.split.map(&:to_i)
k = gets.to_i
b = gets.split.map(&:to_i)
visited = Array.new(n, false)
route = []
cnt = 1
while true
  if cnt == k
    puts b[a-1]
    exit
  end
  if visited[a]
    tmp = route.index(a)
    route.slice!(0,tmp)
    k -= tmp + 1
    break
  end
  visited[a] = true
  route.push(a)
  a = b[a-1]
end
ans_i = k % route.size
puts b[route[ans_i]-1]