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
