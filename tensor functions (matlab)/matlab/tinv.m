function [Ainv] = tinv(A)

%%%  compute the inverse of a n x n x n tensor  %%%
[l,p,n] = size(A);
if((l ~= p) && (l ~= n) && (n ~= p))
    disp('error, tensor is not square')
    return
end

Ainv = fold(inv(tcirc(A)),l,l,l);