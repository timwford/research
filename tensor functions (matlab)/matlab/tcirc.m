function [mA] = tcirc(A)

% function [mA] = tcirc(A);
%
% Take a (n-by-m-by-p) tensor A and slice A from front to back and create 
% an (np -by- mp) block-circulant matrix out of the slices. 
%
% Note: A is a tensor as produced using the Tensor Toolbox.

% Written 2 July 2008

dims = size(A);

n=dims(1);
m=dims(2);
p=dims(3);

mA = zeros(n*p,m*p);

mA(:,1:m) = unfold(A);

for j = 2:p
   mA(:,(j-1)*m+1:j*m) = [mA((p-1)*n+1:p*n,(j-2)*m+1:(j-1)*m); mA(1:(p-1)*n,(j-2)*m+1:(j-1)*m)];
end

