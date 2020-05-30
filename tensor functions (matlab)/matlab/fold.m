function [A] = fold(vA,n,m,p)

% function [A] = fold(vA,n,m,p);
%
% Take a block-vector of (n-by-m) blocks (p of them) and form the
% (n-by-m-by-p) tensor A.
%
% 

% Written 2 July 2008


AA = zeros(n,m,p);
for i = 1:p
    AA(:,:,i) = vA((i-1)*n+1:i*n,1:m);
end

%A = tensor(AA);
A = AA;