"""
Maintainance module for the AeroAgent backend. 
what this module does is that it provides the necessary tools and functionalities to analyze and manage aircraft maintenance data. It includes classes and methods for performing maintenance analysis, generating reports, and providing insights into the maintenance status of aircraft. This module is designed to be used as part of the larger AeroAgent backend system, which aims to streamline and optimize aircraft maintenance processes.
we can simply use this by importing the module and using the classes and methods provided within it. 

this is the trick to convert python code into a package. we can simply use this by importing the module and using the classes and methods provided within it.

"""
from .bedrock_maintenance_analyzer import AircraftMaintenanceAnalyzer
from .engineering_analytics import AircraftEngineeringAnalytics

__all__ = [
    "AircraftMaintenanceAnalyzer",
    "AircraftEngineeringAnalytics"
]

