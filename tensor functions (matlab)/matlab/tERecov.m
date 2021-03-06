function [rho,p] = tERecov(X,S,mu)
%  Compute the energy of a tensor recovered by a given subspace:
%  Usage:  rho = ERecov(X,S)
%  Inputs:  X-tensor, S-singular tuples of the tensor
%  Outputs:  The enrgy recovery

NX = fronorm(X)^2;
[r,c,d] = size(S);

RT = norm(squeeze(S(1,1,:)),'fro')^2;
rho(1) = RT;
for i=2:c
    RT = RT + norm(squeeze(S(i,i,:)),'fro')^2;
    rho(i) = RT;
    if(rho(i)/NX > mu)
        break;
    end
end

rho = rho./NX;
p = i;

