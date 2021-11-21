m = 100
epsilon = 0.1
delta = 0.05
target = function(x){
  return(
    2 * m * exp(-2 * epsilon^2 * x) - delta
  )
}

library('nleqslv')
nleqslv(100, target)