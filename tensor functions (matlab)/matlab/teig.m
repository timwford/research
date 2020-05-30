function [VV,DD]=teig(A)
% tensor-eigendecomposition
% Assumes that each face of the tensor that results after Fourier
% transforming along the 3rd dimension is diagonalizable. 
% 
% Copyright: Misha E. Kilmer, Dec. 2009

[n1,n2,n3]=size(A); 
if n1~=n2
    disp('error, faces are not square')
    return
end

B=fft(A,[],3);

for i=1:n3, 
 [V,D]=eig(B(:,:,i));  %matlab isn't always consistent w/ output ordering.
 delta=diag(D); [delta,jx]=sort(abs(delta),'descend'); 
 V=V(:,jx); D=D(jx,jx); %so, use the same ordering scheme always! This is because we still have to do an ifft. 
 % And it seems it must be
 % this ordering scheme, otherwise the QR iteration returns something
 % different from this code!  
 VV(:,:,i)=V; DD(:,:,i)=D;
 
end

VV=ifft(VV,[],3); DD=ifft(DD,[],3);
end
