import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fname="Session_Trajectory4.txt"

trajectories_all=np.loadtxt(fname)

trials=len(trajectories_all)//3

trials_left=104
trials_right=trials-trials_left

trajectories_left=np.reshape(trajectories_all[:trials_left*3],(trials_left,3,250)) 

trajectories_right=np.reshape(trajectories_all[trials_left*3:],(trials_right,3,250))
fig=plt.figure()
ax=plt.axes(projection='3d')

for traj in trajectories_right:
    ax.plot3D(traj[0],traj[1], traj[2],'r-.', label='Left to Right',alpha=0.07)    
  ##  ax.plot3D(traj[0][0],traj[1][0], traj[2][0],'bo',markersize=20, alpha=0.3, label='Start of the trial')
  ##  ax.plot3D(traj[0][-1],traj[1][-1], traj[2][-1],'ro',markersize=20, alpha=0.3,label='Trial End (Right)')


traj=trajectories_right.mean(axis=0)
ax.plot3D(traj[0],traj[1], traj[2],'r-.', label='Left to Right')    
#ax.plot3D(traj[0][0],traj[1][0], traj[2][0],'bo',markersize=20, alpha=0.3, label='Start of the trial')

traj=trajectories_left.mean(axis=0)
ax.plot3D(traj[0],traj[1], traj[2],'g-.', label='Right to Left')  
#ax.plot3D(traj[0][0],traj[1][0], traj[2][0],'bo',markersize=20, alpha=0.3, label='Start of the trial')

for traj in trajectories_left:
    
    ax.plot3D(traj[0],traj[1], traj[2],color='limegreen', linestyle='dashdot', label='Right to Left', alpha=0.07)
  ##  ax.plot3D(traj[0][0],traj[1][0], traj[2][0],'bo', markersize=20, alpha=0.3) 
  ##  ax.plot3D(traj[0][-1],traj[1][-1], traj[2][-1],'go', markersize=20,alpha=0.3, label='Trial End(Left)')
ax.set(xlabel='Latent dimension 1')

ax.set(ylabel='Latent dimension 2')

ax.set(zlabel='Latent dimension 3')
ax.view_init(elev=0,azim=-40)  

plt.show()
"""
handles, labels = ax.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys())
"""
