
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
        print('Instead using DEFAULT forecast model')
        forecast_model = DefaultBasicForcast()
    
    forecasted_value: float = forecast_model.forecast()
    
    return forecasted_value


class ForecastInterface(ABC):
    @abstractmethod
    def forecast(self) -> float:
        raise NotImplementedError


class BasicForecast(ForecastInterface):
    def __init__(self):
        self.indicator_for_judgment = 1
    # i can give a basic forecast if you don't know modeling
    @abstractmethod
    def forecast(self) -> float:
        return float(20)


class DefaultBasicForcast(BasicForecast):
    def forecast(self) -> float:
        return super().forecast()

# a new forecast model family came, allowing easy variations of forecast


class BetterParentAlgoFore(BasicForecast):
    def __init__(self):
        self.samrter_indicator_for_judgment = 2
    # YOU MUST ABSOLUTELY IMPLEMENT THE METHOD FORECAST


class Var1SmartFor(BetterParentAlgoFore):
    def forecast(self) -> float:
        return float(20 * 2)


if __name__ == "__main__":
    print(temperature_provider())

# # Forecast Logic/Algorithm
# def forecast_tomorrow() -> float:
#     return float(20)

# def forecast_smart_tomorrow() -> float:
#     return float(20 * 2)