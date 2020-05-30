function [P] = tproj(A,U)

% function [P] = tproj(A,U)
%
%Given n x 1 x m tensors A and U, P is the projection of A onto U.  
%NOTE: This assumes U has tensor-length 1, i.e. that 
%
%tprod(tran(U),U) = first column of m x m identity.
%

[n1,n2,n3]=size(A);
[m1,m2,m3]=size(U);

if (n2 ~= 1) | (m2 ~= 1)
	disp('tproj: A and U must have middle dimension = 1.');
	return
end

if (n1 ~= m1) | (n3 ~= m3)
	disp('tproj: A and U must have the same dimensions.');
	return
end

c = tprod(tran(U),A);

P = squeeze(U) * circ(reshape(tran(c),n3,1));




