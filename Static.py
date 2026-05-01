import json
import logging
from datetime import datetime
from os import path
from time import sleep

try:
    if path.getsize("PathToLogFile/Log.log") > 50000000:
        with open("PathToLogFile/Log.log", "w", encoding="utf-8") as f:
            f.write('')
except FileNotFoundError:
    pass
logging.basicConfig(
    filename="PathToLogFile/Log.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

ConfigPathArma = "/PathToServerConfig/config.json"
ScenarioConfig = "/PathToScenarioConfig/WeekScenarioConfig.json"
logging.info(f"Config path: {ConfigPathArma} | Scenario path: {ScenarioConfig}")

while True:
    try:
        with open(ScenarioConfig, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.debug(f"Read {ScenarioConfig} with the scenarios: {data}")
    except Exception as e:
        logging.error(f"Failed to read {ScenarioConfig} with the Exception: {e}")


    scenarios = data["scenarios"]
    tday = datetime.today().strftime("%A").lower()
    scenario = scenarios.get(tday)
    logging.info(f"Scenario: {scenario} for today: {tday}")

    try:
        with open(ConfigPathArma, "r", encoding="utf-8") as f:
            arma_config_scenario = json.load(f)
            logging.debug(f"Content of {ConfigPathArma}: {arma_config_scenario}")
        arma_config_scenario["game"]["scenarioId"] = scenario
        logging.debug(f"Read {ConfigPathArma} with the previous scenario: {arma_config_scenario}")
    except Exception as e:
        logging.error(f"Failed to read {ConfigPathArma} with the Exception: {e}")

    with open(ConfigPathArma, "w", encoding="utf-8") as f:
        json.dump(arma_config_scenario, f, indent=4)
        logging.debug(f"Overwriting {ConfigPathArma} with the content: {arma_config_scenario}")

    logging.debug(f"Scenario: {scenario} for today: {tday}, now sleeping 1Hour")
    sleep(60 * 60 * 1)
exit(1)
