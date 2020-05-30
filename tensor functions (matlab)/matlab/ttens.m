function [C] = ttens(A,B)

% function [C] = ttens(A,B)
%
% Takes tensors A (n -by- m -by- q) and B (m -by- p -by- q) and performs
% the tensor multiplication as defined in Kilmer, Martin and Perrone.  The
% result is a tensor C of with dimensions (n -by- p -by- q).
%
% Note: A is a tensor as produced using the Tensor Toolbox.

% Written 2 July 2008

dimsA = size(A);
dimsB = size(B);

if length(dimsB) == 2
    dimsB = [dimsB(1) 1 dimsB(2)];
end

n = dimsA(1);
m = dimsA(2);
q = dimsA(3);
p = dimsB(2);

if (dimsB(1) ~= m) || (dimsB(3) ~= q)
    disp('Incompatible dimensions.');
    return
end

C = fold ( tcirc(A)*unfold(B), n, p, q);

