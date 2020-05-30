function C=tprod(A,B)

% C = tprod(A,B)
%
% compute the tensor-tensor product using FFTs
% A is n1 x n2 x n3; B is na x n4 x nb; then 
% output is n1 x n4 x n3
% 
% Follows multiplication defined in Kilmer, Martin and Perrone, 2008
% 
% Copyright: Misha E. Kilmer


[n1,n2,n3]=size(A);
[na,n4,nb]=size(B);

if n3~=nb|n2~=na
    disp('WARNING, dimensions are not acceptable')
    return
end

D=fft(A,[],3); %faces are Di's
Bhat=fft(B,[],3); 

for i=1:n3
    C(:,:,i)=D(:,:,i)*Bhat(:,:,i);
end

C=ifft(C,[],3);
