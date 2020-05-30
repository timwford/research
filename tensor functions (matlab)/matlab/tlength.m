function [len] = tlength(X)

%function [len] = tlength(X)
%
%Given an m x 1 x n tensor A, i.e. a vector of n-tuples, 
%len = the length of X as defined in 'newpaper'.  
%
%

[m,p,n]=size(X);


if (p ~= 1)
	disp('tlength: X must have middle dimension = 1.');
	return
end

c = tprod(tran(X),X);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% This is using Misha's definition from 'newpaper' %%%%%%%%%%%%%%
%len = norm(squeeze(c),'fro')/norm(squeeze(X),'fro');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  If we consider K_n as a C*-algebra (i.e. Banach space + involutive
%  associative algebra), though, the inner product on K_n^m
%  maps into K_n ('positive' is defined relative to the C*-algebra) and
%  the norm on K_n is just the usual Banach space norm, i.e. the 2-norm
%  (which equals the Frobenius norm on K_n).
%
%  So, length of X in K_n^m should be:
%
%  len(X) = sqrt( norm ( inner product of X & X^T ) )
%         = sqrt( norm ( tprod(trans(X),X) ) )
%
%  Updated: 7/8/10, KSB
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

len = sqrt( norm ( squeeze(c) ) );

