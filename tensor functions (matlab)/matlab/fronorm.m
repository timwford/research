function y = fronorm(A)
%frobenius norm of a tensor

tmp=A.*A;
y = sqrt(sum(abs(tmp(:))));

