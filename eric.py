
from febo.controller import SimpleController
from febo.algorithms import Random
from febo.environment.benchmarks.hpolib import Camelback

from febo.controller.simple import SimpleControllerConfig
# Setup
SimpleControllerConfig.T = 1000

s = SimpleController(algorithm=Random(), environment=Camelback())

s.initialize()
s.run()