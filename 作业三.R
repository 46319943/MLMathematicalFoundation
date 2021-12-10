theta = 0.1
d = 8
Ein = 0.008

target = function(n){
  return(
    theta^2 * (1 - (d + 1) / n) - Ein
  )
}

library('nleqslv')
nleqslv(10, target)



err = function(u, v){
  return(
    exp(u) + exp(2*v) + exp(u*v) + u^2 - 2*u*v + 2*v^2 - 3*u - 2*v
  )
}
gradient_u = function(u, v){
  return(
    exp(u) + v*exp(u*v) + 2*u - 2*v - 3
  )
}
gradient_v = function(u, v){
  return(
    2*exp(2*v) + u*exp(u*v) + 2*u + 4*v - 2
  )
}
u0 = 0
v0 = 0
u = u0
v = v0
u_last = u0
v_last = v0
Eta = 0.01
for(i in 1:5){
  u = u - Eta*gradient_u(u_last, v_last)
  v = v - Eta*gradient_v(u_last, v_last)
  u_last = u
  v_last = v
}
err(u, v)



Ein_sum = 0
wlin_sum = rep(0, 6)
Ein_sum_t = 0
for(i in 1:1000){
  x1 = runif(1000, -1, 1)
  x2 = runif(1000, -1, 1)
  y = sign(x1^2 + x2^2 - 0.6)
  flip_index = sample(1:1000, 100)
  y[flip_index] =  - y[flip_index]
  X = cbind(
    rep(1, 1000),
    x1,
    x2
  )
  library('pracma')
  pseudo_inverse_X = pinv(X)
  wlin = pseudo_inverse_X %*% y
  y_hat = sign(X %*% wlin)
  Ein = mean(y != y_hat)
  Ein_sum = Ein_sum + Ein
  
  x1x2 = x1 * x2
  x1_2 = x1^2
  x2_2 = x2^2
  X = cbind(
    X,
    x1x2,
    x1_2,
    x2_2
  )
  pseudo_inverse_X = pinv(X)
  wlin = pseudo_inverse_X %*% y
  wlin_sum = wlin_sum + wlin
  y_hat = sign(X %*% wlin)
  Ein = mean(y != y_hat)
  Ein_sum_t = Ein_sum_t + Ein
  
}
Ein_average = Ein_sum / 1000
wlin_average = wlin_sum / 1000
Ein_average_t = Ein_sum_t / 1000


