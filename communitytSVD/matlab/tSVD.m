function [U,S,V]=t_SVD(A,k)
% compute the full t-SVD of tensor A if k is unspecified or non-zero
% compute the compact t-SVD of tensor A if fl is zero
% compute the truncated (to k terms) t-SVD if k is specified and non-zero.
% Follows the T-svd given in Kilmer, Martin and Perrone, 2008
%
% Copyright: Misha E. Kilmer; revised for partial tsvd, June 2009


[n1,n2,n3]=size(A);

disp("Size of A")
disp(size(A))

if n2 > n1
    transflag=1;
    A=tran(A);
    nn1=n1;
    n1=n2;
    n2=nn1;
end

A=fft(A,[],3);

disp("Size of A FFT")
disp(size(A))

fl=1;

if nargin ==2
    if k==0
        fl=0;
    end
end


for i=1:n3
    if fl==0
      [U1,S1,V1]=svd(A(:,:,i),0);  
      U(:,:,i)=U1; S(:,:,i)=S1; V(:,:,i)=V1;
    else
      [U1,S1,V1]=svd(A(:,:,i));
      if nargin == 2 
       U(:,:,i)=U1(:,1:min(k,n1));
       S(:,:,i)=S1(1:min(k,n1),1:min(k,n2));
       V(:,:,i)=V1(:,1:min(k,n2));
      else
          U(:,:,i)=U1; V(:,:,i)=V1; S(:,:,i)=S1;
      end
      
    end
    
end

disp("Size of U")
disp(size(U))


U=ifft(U,[],3); V=ifft(V,[],3); S=ifft(S,[],3);

disp("Size of U ifft")
disp(size(U))


if exist('transflag','var')
    Uold =U; U=V; S=tran(S); V=Uold;  
end
