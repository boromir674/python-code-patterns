
# Service 2
# I provide temperature of tomorrow

from abc import abstractmethod, ABC
from typing import Type


def temperature_provider() -> float:
    # forecasted_value: float = forecast_tomorrow()
    try:
        forecast_model = BetterParentAlgoFore()
    except TypeError as e:
        print("error instantiating class better parent algo fore")
        forecast_model = DefaultBasicForcast()
    
    forecast_model = TemperatureComputer(forecaster=forecast_model)
    
    forecasted_value: float = forecast_model.compute()
    
    return forecasted_value


class ForecastInterface(ABC):
    @abstractmethod
    def forecast(self) -> float:
        raise NotImplementedError

class TemperatureComputer():
    forecaster: ForecastInterface

    def __init__(self, forecaster) -> None:
        self.forecaster = forecaster
    
    def compute(self) -> float:
        return self.forecaster.forecast()


class BasicForecast(ForecastInterface):
    def __init__(self):
        self.indicator_for_judgment = 1
    # i can give a basic forecast if you don't know modeling

class DefaultBasicForcast(BasicForecast):
    def forecast(self) -> float:
        return float(20)


# a new forecast model family came, allowing easy variations of forecast
class BetterParentAlgoFore(BasicForecast):
    def __init__(self):
        self.samrter_indicator_for_judgment = 2
    # YOU MUST ABSOLUTELY IMPLEMENT THE METHOD FORECAST


# this uses the old logic using the default basic forecast
# this is a rare case that uses old logic to create a new forecast
class OldLogicToNewLogic(DefaultBasicForcast):
    def forecast(self) -> float:
        old_forecast = super().forecast()
        return float(old_forecast * 2)


class Var1SmartFor(BetterParentAlgoFore):
    def forecast(self) -> float:
        return float(20 * 100)


if __name__ == "__main__":
    print(temperature_provider())
