function Z=tran(A)
% return the tensor transpose of A, using definition
% in Kilmer, Martin and Perrone, 2008
%
% Dependencies: fold_up.m
% 
% Copyright: Misha E. Kilmer

[n1,n2,n3]=size(A);
idx=[1,n3:-1:2];     %order faces 1,n3,n3-1,n3-2,...,2
  %note, each face is n1 x n2.  So its transpose is n2 x n1 and the
  % transposed tensor is thus n2 x n1 x n3
  
jknt=0;
Y=zeros(n3*n2,n1);  
for j=1:n3
    Y(jknt+1:jknt+n2,1:n1)=A(:,:,idx(j))'; %take conjtrans of ea. face.
    jknt=jknt+n2;
end

Z = fold_up(Y,n2,n1,n3);

