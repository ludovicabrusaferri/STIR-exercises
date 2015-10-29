# -*- coding: utf-8 -*-
"""
Example script to serve as starting point for display the results of the brain simulation

The current script reads results from run_scatter0 and displays them comparing 
with the truth (i.e. simulation input and simulation scatter output)

Author: Kris Thielemans
"""
#%% Initial imports
import matplotlib.pyplot as plt
import stir
from stirextra import *
import os
#%% go to directory with input files
# adapt this path to your situation (or start everything in the exercises directory)
os.chdir('/home/stir/stir-exercises')
#%% run simulation (if you haven't done it yet)
print(os.popen('./run_simulation_SPECT.sh').read())
#%% change directory to where the output files are.
os.chdir('working_folder/single_slice_SPECT')
#%% Read in images
image=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('emission.hv'));
mu_map=to_numpy(stir.FloatVoxelsOnCartesianGrid.read_from_file('CTAC.hv'));
#%% bitmap display of images
slice=0;
plt.figure();
ax=plt.subplot(1,2,1);
plt.imshow(image[slice,:,:,]);
plt.colorbar();
plt.axis('off');
ax.set_title('emission image');

ax=plt.subplot(1,2,2);
plt.imshow(mu_map[slice,:,:,]);
plt.colorbar();
plt.axis('off');
ax.set_title('attenuation image');

#%% read in sinograms
# simulated data
sinogram=to_numpy(stir.ProjData.read_from_file('my_sim.hs'));
# after adding some noise
noisy_sinogram=to_numpy(stir.ProjData.read_from_file('my_noise.hs'));
#%% Display bitmaps of a middle sinogram
# When you compare this to PET sinograms, is the angle (theta) range the same? 
# (open the header of a sinogram, e.g. my_sim.hs, to check what the range is for this 
# SPECT sinogram)
maxforplot=sinogram.max();

slice=0; # single sinogram only, but returned as a 3D array
plt.figure()
ax=plt.subplot(1,2,1);
plt.imshow(sinogram[slice,:,:,]);
plt.clim(0,maxforplot)
ax.set_title('simulation');
plt.axis('off');

ax=plt.subplot(1,2,2);
plt.imshow(noisy_sinogram[slice,:,:,]);
plt.clim(0,maxforplot);
ax.set_title('noisy');
plt.axis('off');
#%% Display central horizontal profiles through the sinogram
plt.figure()
plt.plot(sinogram[slice,128/2,:],'b');
plt.hold(True)
plt.plot(noisy_sinogram[slice,128/2,:],'c');
plt.legend(('simulation','with added noise'));
#%% What to do now?
# - make a copy of the files to a new directory
#  and edit the new forward_projector_SPECT.par to change PSF parameters
#  and/or simulate_data.sh to change the amount of noise
# (run poisson_noise without arguments to get a usage message)
#  Then simulate again via the command
#    ./simulate_data.sh emission.hv CTAC.hv template_sinogram.hs
#%% close all plots
plt.close('all')