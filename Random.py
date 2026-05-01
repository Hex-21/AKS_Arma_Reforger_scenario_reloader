import json
import logging
import random
import time

ConfigPathArma = "/pathtoconfig/config.json"
ScenarioConfig = "/pathtoreloaderconfig/ScenarioConfig.json"

logging.basicConfig(
    filename="/pathforlogs/Log.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

while True:
    with open(f"{ScenarioConfig}", "r") as f:
        config = json.load(f)
        maps = config['scenarios']


    with open(f"{ConfigPathArma}", "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
    random_map = random.choice(maps)
    config['game']['scenarioId'] = f"{random_map}"
    logging.info(f"Scenario '{random_map}' loaded in config")

    with open(f"{ConfigPathArma}", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    time.sleep(60*60*12)  # 12H
