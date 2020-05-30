function [It] = teye(n)
%%%  Create an n x n x n identity tensor  %%%

Im = eye(n,n);

It = zeros(n,n,n);
It(:,:,1) = Im;