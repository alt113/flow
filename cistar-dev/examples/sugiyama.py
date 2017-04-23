import logging

from cistar.core.exp import SumoExperiment
from cistar.envs.loop_accel import SimpleAccelerationEnvironment
from cistar.scenarios.loop.loop_scenario import LoopScenario
from cistar.controllers.car_following_models import *
from cistar.controllers.lane_change_controllers import *

logging.basicConfig(level=logging.INFO)

sumo_params = {"port": 8873, "time_step":0.01, "emission_path": "./data/"}

sumo_binary = "sumo"

type_params = {"ovm": (12, (OVMController, {}), (StaticLaneChanger, {}), 0)}

env_params = {"target_velocity": 25}

net_params = {"length": 500, "lanes": 1, "speed_limit":35, "resolution": 40, "net_path":"debug/net/"}

cfg_params = {"start_time": 0, "end_time":3000, "cfg_path":"debug/cfg/"}

initial_config = {"shuffle":False, "bunching":200}

scenario = LoopScenario("single-lane-one-contr", type_params, net_params, cfg_params, initial_config)

leah_sumo_params = {"port": 8873}

exp = SumoExperiment(SimpleAccelerationEnvironment, env_params, sumo_binary, sumo_params, scenario)

logging.info("Experiment Set Up complete")

exp.run(1, 1000)

exp.env.terminate()
