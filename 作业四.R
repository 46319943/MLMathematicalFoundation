p = sqrt(sqrt(3) + 4)
p = sqrt(sqrt(3) - 1)
p = sqrt(9 + 4*sqrt(6))
x0 = c(1,1,1)
x1 = c(-1, p, 1)
y = c(0, 1, 0)
E_loocv = 0
X = cbind(
  x0,
  x1
)
library('pracma')

pseudo_inverse_X = pinv(X[1:2,])
wlin = pseudo_inverse_X %*% y[1:2]
E_loocv = E_loocv + (X[3,] %*% wlin - y[3])^2

pseudo_inverse_X = pinv(X[c(1,3),])
wlin = pseudo_inverse_X %*% y[c(1,3)]
E_loocv = E_loocv + (X[2,] %*% wlin - y[2])^2

pseudo_inverse_X = pinv(X[2:3,])
wlin = pseudo_inverse_X %*% y[2:3]
E_loocv = E_loocv + (X[1,] %*% wlin - y[1])^2

