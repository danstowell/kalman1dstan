/*
cd ~/dev/stan/stan
make ~/git/stored_docs/dev/stan/kalman/kalman1d

cd ~/git/stored_docs/dev/stan/kalman/
./kalman1d --data=kalman1d.data.R
*/
data {
	int<lower=0> N;
	real y[N];
}
parameters {
	real x[N];

	real f_trans;
	real f_off;
	real<lower=0> f_noise;

	real h_off;
	real h_trans;
	real<lower=0> h_noise;
}
model {
	for (n in 2:N)
		x[n] ~ normal(f_off + (f_trans * x[n-1]), f_noise);
	for (n in 1:N)
		y[n] ~ normal(h_off + (h_trans * x[n]), h_noise);
}

