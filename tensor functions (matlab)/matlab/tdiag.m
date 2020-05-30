function [X,L,Xinv] = Tdiag(A)

% function [X,L,Xinv] = Tdiag(A);
%
% Compute the tensor diagonalization of tensor A an (n x n x p) tensor.
%
% Note: A should be of type 'tensor' as produced by the tensor command from
% the Tensor Toolbox.

% Written 2 July 2008

dims = size(A);

n=dims(1);
m=dims(2);
p=dims(3);

if n ~= m
    disp('First two dimensions of A must be equal.');
    exit
end

mA = tcirc(A);

 F = kron( fft(eye(n,n)),eye(n,n));
iF = kron(ifft(eye(n,n)),eye(n,n));

D = F*mA*iF;

DX    = zeros(n*p,n*p);
DXinv = zeros(n*p,n*p);
DL    = zeros(n*p,n*p);

for i=1:p
    [DX((i-1)*n+1:i*n,(i-1)*n+1:i*n), DL((i-1)*n+1:i*n,(i-1)*n+1:i*n)] = ...
        eig(D((i-1)*n+1:i*n,(i-1)*n+1:i*n));
    DXinv((i-1)*n+1:i*n,(i-1)*n+1:i*n) = inv( DX((i-1)*n+1:i*n,(i-1)*n+1:i*n) );
end

XX = iF*DX*F;
LL = iF*DL*F;
XXinv = iF*DXinv*F;

X = fold(XX,n,m,p);
L = fold(LL,n,m,p);
Xinv = fold(XXinv,n,m,p);
