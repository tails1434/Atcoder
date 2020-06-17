N = gets.to_i
EDGE = Array.new(N){[]}

N.times do |i|
  if i == N - 1
    next
  end
  a, b = gets.split.map(&:to_i)
  a -= 1
  b -= 1
  EDGE[a].push(b)
  EDGE[b].push(a)
end

DP = Array.new(N+5){Array.new(2,0)}
MOD = 10 ** 9 + 7
def dfs(s,c,p)
  if DP[s][c] == 0
    ret = 1
    EDGE[s].each do |v|
      if p == v
        next
      end
      if c == 0
        ret *= (dfs(v,0,s) + dfs(v,1,s))
      else
        ret *= dfs(v,0,s)
      end
    end
    DP[s][c] = ret % MOD
  end
  return DP[s][c]
end

ans = dfs(0,0,0) + dfs(0,1,0)
puts ans % MOD