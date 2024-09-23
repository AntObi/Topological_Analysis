"""This module contains the configuration parameters for the Topological Analysis package."""

from ruamel.yaml import YAML
import os
import Topological_Analysis
# Load the radii file
yaml = YAML()
va_dir = os.path.dirname(Topological_Analysis.__file__)
radii_yaml_dir = os.path.join(va_dir, 'files/radii.yaml')
with open(radii_yaml_dir, 'r') as f:
    RADII = yaml.load(f)