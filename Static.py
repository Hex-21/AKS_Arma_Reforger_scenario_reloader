# Loading scenarios from top to bottom(ScenarioConfig)
import json
import logging
import random
import time

ConfigPathArma = "/pathtoconfigfile.conf"
ScenarioConfig = "./ScenarioConfig.json"

logging.basicConfig(
    filename="Log.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

while True:
    with open(f"{ScenarioConfig}", "r") as f:
        config = json.load(f)
        maps = config['scenarios']

    for map in maps:
        with open(f"{ConfigPathArma}", "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
            config['game']['scenarioId'] = f"{map}"

        with open(f"{ConfigPathArma}", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
            logging.info(f"Scenario '{map}' loaded in config")
        time.sleep(60 * 60 * 24 * 1)  # 48H (60*60*24*1) #60(Sekunden)*60(Minuten)*24(Stunden)*(Tage)
