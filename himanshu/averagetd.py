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

plt.xlabel('Latent Dimeanion 1')

plt.ylabel('Latent Dimeanion 2')

for traj in trajectories_right[0:50:5]:
    plt.plot(traj[0], traj[1],'r-.',alpha=0.3)


traj=trajectories_right[0:50:5].mean(axis=0)
plt.plot(traj[0], traj[1],'r', label='Left to Right')

#traj=trajectories_left.mean(axis=0)
plt.plot(traj[0][0], traj[1][0],'go',markersize=20,alpha=0.3, label='Trial Start')

plt.plot(traj[0][-1], traj[1][-1],'bo',markersize=20,alpha=0.3, label='Trial End')
#for traj in trajectories_left:

 #   plt.plot(traj[0], traj[1],color='limegreen', linestyle='dashdot', label='Right to Left', alpha=0.03)
plt.title('Trial Averaged Trajectories for Right Motion Trials')
plt.legend()
plt.show()
