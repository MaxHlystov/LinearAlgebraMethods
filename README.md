# LinearAlgebraMethods
Some functions to solve linear algebra problems

## GaussElimination.py
Solve system of linear equation by Gaussian elimination method (see https://en.wikipedia.org/wiki/Gaussian_elimination) 

## bestLinearSystemSolution.py
Find the best system of linear equation solution by minimize squared difference between vector of the constant terms and computed by the system values.  
For example, we have some linear model Y=C*X.  
Where Y - vector of outputs (size n*1);  
  X - vector of inputs (size n*m);  
  C - vector of coefficients (size m).  
If we want to find coefficients, which will give the best output by given input vector x (m - count of inputs), we need to make a lot of measurements (size n). And we will take two vectors X (inputs) and Y (mesured outputs). One row of the vectors is a measure. Then we found by findBestSolution() function vector of coefficients, that best predicts outputs y by any x vector of inputs.  
