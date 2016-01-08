#!/bin/sh
# @Author: pchambers
# @Date:   2016-01-08 17:35:49
# @Last Modified by:   pchambers
# @Last Modified time: 2016-01-08 17:54:57

# Create the Conda test environment
conda create --name jenkins_example_pytest python=2
source activate jenkins_example_pytest

pip install -e Example_pytest
cd Example_pytest
py.test -v

# Clean the Conda test environment
source deactivate
conda env remove -n jenkins_example_pytest