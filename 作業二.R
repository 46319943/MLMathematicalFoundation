epsilon = 0.05
dvc = 10
delta = 0.05
target = function(x){
  return(
    sqrt(
      (8/x) * log(4 * (2*x)^dvc / epsilon)
    ) - delta
  )
}

library('nleqslv')
nleqslv(10000, target)

epsilon = 0.05
dvc = 50
n = 5

vc_bound = function(){
  return (
    sqrt(
      8 / n * log(4 * (2*n)^dvc / epsilon)
    )
  )
}
vc_bound()

rademacher_penalty_bound = function(){
  return (
    sqrt(2 * log(2 * n * n^dvc) / n) 
    + sqrt(2 / n * log(1 / epsilon)) 
    + 1/n
  )
}
rademacher_penalty_bound()

parrondo_and_van_den_broek = function(delta){
  return (
    sqrt(
      1 / n * (2*delta + log(6 * (2*n)^dvc / epsilon))
    ) - delta
  )
}
nleqslv(delta, parrondo_and_van_den_broek)

# 需要对Log化简，不然log项中的(N^2)^dvc为Inf
# 需要先把平方拿到外面来
devroye = function(delta){
  return (
    sqrt(
      1 / (2*n) * (4*delta * (1 + delta) + log(4) - log(epsilon) + 2*dvc*log(n))
    ) - delta
  )
}
nleqslv(delta, devroye)

varint_vc_bound = function(){
  return(
    sqrt(
      16 / n * log(2 * n^dvc / sqrt(epsilon))
    )
  )
}
varint_vc_bound()