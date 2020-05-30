n = 10;

figure;
for i = 1:24
  A = round(rand(n));
  A = triu(A) + triu(A,1)';
  A = A - diag(diag(A));
  [U,S,V] = svd(A);
  %Um(:,i,:) = U(:,1:2);
  TG(:,i,:) = A;
end


[U,S,V] = svd(A);

disp(size(TG))

M = U(:,1:2)'*A;

figure;
plot(M(1,:),M(2,:),'r*','markersize',4)