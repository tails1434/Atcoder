class Array
  alias_method :enqueue, :push
  alias_method :dequeue, :shift
end

H, W = gets.split.map(&:to_i)
A = N.times.map{gets.split.map(&:to_i)}.transpose
visited = Array.new(N){Array.new(N,false)}



MOD = 10 ** 9 + 7