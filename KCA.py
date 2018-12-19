import numpy as np, matplotlib.pyplot as pp
from pykalman import KalmanFilter
def fitKCA(t,z,q,fwd=0):
    #
    #Inputs:
    #    t: Iterable with time indices
     #   z: Iterable with measurements
    #    q: Scalar that multiplies the seed states covariance
     #   fwd: number of steps to forecast (optional, default=0)
    #Output:
    #x[0]: smoothed state means of position velocity and acceleration
    #x[1]: smoothed state covar of position velocity and acceleration
    #Dependencies: numpy, pykalman
    #
#1) Set up matrices A,H and a seed for Q
	h=(t[-1]-t[0])/t.shape[0]
	A=np.array([[1,h,.5*h**2],
            [0,1,h],
            [0,0,1]])
	Q=q*np.eye(A.shape[0])
#2) Apply the filter
	kf=KalmanFilter(transition_matrices=A,transition_covariance=Q)
	kf=kf.em(z)
#4) Smooth
	x_mean,x_covar=kf.smooth(z)
#5) Forecast
	for fwd_ in range(fwd):
		x_mean_,x_covar_=kf.filter_update(filtered_state_mean=x_mean[-1], filtered_state_covariance=x_covar[-1])
		x_mean=np.append(x_mean,x_mean_.reshape(1,-1),axis=0)
		x_covar_=np.expand_dims(x_covar_,axis=0)
		x_covar=np.append(x_covar,x_covar_,axis=0)
#6) Std series
	x_std=(x_covar[:,0,0]**.5).reshape(-1,1)
	for i in range(1,x_covar.shape[1]):
		x_std_=x_covar[:,i,i]**.5
		x_std=np.append(x_std,x_std_.reshape(-1,1),axis=1)
	return x_mean,x_std,x_covar
	
def getPeriodic(periods,nobs,scale,seed=0):
	t=np.linspace(0,np.pi*periods/2.,nobs)
	rnd=np.random.RandomState(seed)
	signal=np.sin(t)
	z=signal+scale*rnd.randn(nobs)
	return t,signal,z
	
def plots():
	nobs,periods,frac=300,10,[.5,.25,.1]
	t,signal,z=getPeriodic(periods,nobs,scale=.5)
	x_point,x_bands=fitKCA(t,z,q=.001)[:2]
	pp.plot(t,z,marker='o',linestyle='',label='measurements')
	pp.plot(t,signal,marker='x',linestyle='',label='Signal')
	pp.plot(t,x_point[:,0],marker='o',linestyle='-',label='KCA position')
	pp.show()
	
plots()