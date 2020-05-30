function [vA] = unfold(A)

% function [vA] = unfold(A);
%
% Slice A from front to back and create a block-vector out of the slices 
%
% Note: A should be of type 'tensor' as produced by the tensor command from
% the Tensor Toolbox.

% Written 2 July 2008

dims = size(A);

n=dims(1);
m=dims(2);
p=dims(3);

vA = zeros(n*p,m);
for i = 1:p
    vA((i-1)*n+1:i*n,1:m) = A(:,:,i);
end

