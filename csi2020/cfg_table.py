#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Configuration table
  ~~~~~~~~~~~~~~~~~~~

"""

import os
import time

# ------------------------------------------------------------------------------
# Configuration table
# ------------------------------------------------------------------------------
cfg = {
  'data_root':r'e:\data',
  'roi_x' : 1900,
  'roi_y' : 1020,
  'fullimage_x' : 1968,
  'fullimage_y' : 1112,
  'saveimages' : 0,
  'DarkStartInt' : 20,
  'DarkStopInt'  : 60020,
  'DarkStepInt' : 30000,
  'DarkFrames' : 50,
  'LightStartInt' : 0,
  'LightStopInt': 800,
  'LightStepInt': 40,
  'LightFrames': 50,
  'LagCapturedFrames': 100,
  'QEStartW': 400,
  'QEStopW': 1000,
  'QEStepW': 10,
  'QEFrames': 25,
  'QEDarkCal': 25,
  'QEIntTime': 1100,
  'MTF_start_wavelength': 400,
  'MTF_stop_wavelength': 1000,
  'MTF_step_size': 100,
  'MTF_stop': 0.005,
  'MTF_stage_step': 0.0002,
  'MTF_num_images': 20,
  'MTF_offset': 0.02,
  'sensor_pos': 0,
  'wavelength': 520,
  'wavetablename': r'c:\\temp\\WaveTable_blackmagic.csv',
  'test_name': 'dvt',
  'PID': 'Hwk1910',
  'shutter': 1,
  'ptc_int': 20,
  'setmode': 'hg',
  'SysClock': 74500000,
  'camera_comport': 5,
  'pythondir': r'C:\CIS2051\Testcam\PythonScripts',
  'pythonexecpath': r'c:\python27',
  'mightex_comport': 5,
  'mightex_channel': 2,
  'mightex_ch1_limit': 1000,
  'mightex_ch2_limit': 1000,
  'mightex_ch3_limit': 0,
  'mightex_ch4_limit': 0,
  'use_custom_python': 0,
  'custom_python_script': 'blah.py',
  #[analysis_parameters]
  'xstart': 1,
  'ystart': 1,
  'xsubimage': 1900,
  'ysubimage': 1020,
  'xave': 1,
  'yave': 1,
  'pt_ll': 0.2,
  'pt_ul': 0.8,
  'prstats_psat': 0.9,
  'prnu_psat': 0.5,
  'fwc_nl_bound': 0.02,
  'nei_psat': 0.85,
  'ic_cal_point': 0.5,
  'ic_fpn_measurement_points': 0.25,  #0.75
  'ic_mode': 0,
  'lag_mode': 0,
  'photon_transfer': 1,
  'dark_current': 1,
  'qe': 0,
  'lag': 0,
  'mtf': 0,
  'cte': 0,
  'nei': 0,
  'ic': 0,
  'blemish_detect': 0,
  'blemish_correct': 0,
  'image_stats_save_result_images': 1,
  'image_stats_number_of_bootstrap_iterations': 8,
  'image_stats_functions': 'median,mean,mode,std,rms_nu,p2p_nu',
  'blemish_detect_functions': 'gblemd_mdf,gblemd_mlf',
  'blemish_correct_function': 'gblemc',
  #[data_files]
  'photon_transfer': r'C:\data\l3cis5\1r5\Light\cfg\l3cis5_1r5__ptc_D6_19_2008_T6_59_36PM.ini',
  'dark_current': r'C:\Labview\cfg\L3CIS3\results\dark_current\dark_current.cfg',
  'qe_dark': r'e:\data\CIS2051\CIS2051_W_D_SNes0550248_rhgt_100MHz_rs_D1_15_2010_T11_36_48AM\dvt\cfg\CIS2051_CIS2051_W_D_SNes0550248_rhgt_100MHz_rs_D1_15_2010_T11_36_48AM_dvt___dark_wv_D1_15_2010_T11_36_48AM.ini',
  'qe_light': r'e:\data\CIS2051\CIS2051_W_D_SNes0550248_rhgt_100MHz_rs_D1_15_2010_T11_36_48AM\dvt\cfg\CIS2051_CIS2051_W_D_SNes0550248_rhgt_100MHz_rs_D1_15_2010_T11_36_48AM_dvt___light_wv_D1_15_2010_T11_36_48AM.ini',
  'lag': r'c:\Labview\cfg\cameratest\CIS2051\tests\lag_file.ini',
  'mtf': 'null',
  'cte': 'null',
  'nei': 'null',
  'ic': 'ic_files.ini',
  'ic_cal': 'ic_cal_file.ini',
  'ic_cal_infile': 'null',
  'ic_cal_outfile': 'null',
  'blemish_detect': r'e:\data\l3cis5\7\dvt\cfg\blemish_files.ini',
  'blemish_map': 'blemish_file.txt',
  'output': r'C:\data\l3cis5\1r5\Light\results\output.txt',
  'binaryformat': 0,
  'BigEndianImage': 1,
  'NumberOfBitsPerPixel': 12,
  'debug': 0,
  'syslog': r'C:\data\l3cis5\1r5\Light\results\syslog.txt',
  #[sensor_parameters]
  'xsize': 1900,
  'ysize': 1020,
  'txsize': 1900,
  'tysize': 1020,
  'txstart': 1,
  'tystart': 1,
  'tos_xsize': 1900,
  'tos_ysize': 1020,
  'tos_xstart': 1,
  'tos_ystart': 1,
  'pixel_area': 0.000000254016,
  'tint_nom': 0.0327,
  'conversion_gain_default': 1.73,
  'use_default_cg': 0,
}
# ------------------------------------------------------------------------------
# End of configuration file
# ------------------------------------------------------------------------------      

"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
