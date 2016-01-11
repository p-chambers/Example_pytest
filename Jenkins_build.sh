#!/bin/bash
# @Author: pchambers
# @Date:   2016-01-08 17:35:49
# @Last Modified by:   pchambers
# @Last Modified time: 2016-01-08 18:40:15

# Create the Conda test environment (note that pytest is required, otherwise wrong
# python is used and the module is not found!)
conda create --name jenkins_example_pytest python=2 pytest
source activate jenkins_example_pytest

python setup.py install
py.test -v

# Clean the Conda test environment
source deactivate
conda env remove -n jenkins_example_pytest
