function [tA] = trans(A)

% function [mA] = tcirc(A);
%
% Take a (n-by-m-by-p) tensor A and build the (m-by-n-by-p) tensor 
% transpose of A.

% Written 11 Jan 2010

dims = size(A);

n=dims(1);
m=dims(2);
p=dims(3);

tA = zeros(m,n,p);

tA(:,:,1) = A(:,:,1)';

for j = p:-1:2
   tA(:,:,p-j+2) = A(:,:,j)';
end

