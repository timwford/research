function Y=fold_up(A,n1,n2,n3)

% Y=fold_up(A,n1,n2,n3)
%
% fold the array in A back up into a tensor.
% A should be n1*n3 x n2
 
 knt=0; Y=zeros(n1,n2,n3);
 
 for i=1:n3
     Y(:,:,i)=A(knt+1:knt+n1,1:n2); knt=knt+n1;
 end
