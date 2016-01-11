#!/bin/bash
# @Author: pchambers
# @Date:   2016-01-08 17:35:49
# @Last Modified by:   pchambers
# @Last Modified time: 2016-01-08 18:40:15

# Tell the system where conda is: MOVED TO ENVIRONMENT VARIABLES IN JENKINS 
# export PATH="/home/pchambers/anaconda2/bin:$PATH"

# Check which python will be used
which python

# Create the Conda test environment
conda create --name jenkins_example_pytest python=2
source activate jenkins_example_pytest

# Check which python will be used (should now be jenkins_home/.conda/ somewhere)
which python

python setup.py install
py.test -v

# Clean the Conda test environment
source deactivate
conda env remove -n jenkins_example_pytest
