class PriorityQueue
  attr_reader :size

  def initialize
    @heap = []
    @size = 0
  end

  def add(n)
    i = @size
    while i > 0 do
      parent_index = (i - 1) / 2
      break if n >= @heap[parent_index]

      @heap[i] = @heap[parent_index]
      i = parent_index
    end

    @heap[i] = n
    @size += 1
  end

  def pop
    return if @size <= 0
    min_n = @heap[0]
    @size -= 1
    n = @heap[@size]
    i = 0
    while i * 2 + 1 < @size do
      child_index1 = i * 2 + 1
      child_index2 = i * 2 + 2
      if child_index2 < @size && @heap[child_index2] < @heap[child_index1]
        child_index1 = child_index2
      end
      break if @heap[child_index1] >= n

      @heap[i] = @heap[child_index1]
      i = child_index1
    end
    @heap[i] = n
    min_n
  end

  def min; @heap[0] end
  def values; @heap.first(@size) end
  def inspect; "Heap: #{values}" end
  def size; @size end
end

def dijkstra_heap(s,edge,n)
  d = Array.new(n, 10**20)
  used = Array.new(n, true)
  d[s] = 0
  used[s] = false
  edgelist = PriorityQueue.new
  edge[s].each do |a, b|
    edgelist.add(a*(10**6)+b)
  end
  while edgelist.size != 0
    minedge = edgelist.pop
    if !used[minedge % (10**6)]
      next
    end
    v = minedge % (10**6)
    d[v] = minedge / (10 ** 6)
    used[v] = false
    edge[v].each do |e|
      if used[e[1]]
        edgelist.add((e[0]+d[v])*(10**6)+e[1])
      end
    end
  end
  return d
end

N, M, T = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
edge = Array.new(N){[]}
re_edge = Array.new(N){[]}
M.times do |i|
  a, b, c = gets.split.map(&:to_i)
  a -= 1
  b -= 1
  edge[a].push([c,b])
  re_edge[b].push([c,a])
end

go = dijkstra_heap(0, edge, N)
back = dijkstra_heap(0, re_edge, N)

d = Array.new(N,0)
N.times do |i|
  d[i] = T - (go[i] + back[i])
end

ans = Array.new(N,0)
N.times do |i|
  if d[i] > 0
    ans[i] = A[i] * d[i]
  end
end
puts ans.max