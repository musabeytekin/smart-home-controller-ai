from langchain_core.tools import tool


@tool
def adjust_temperature(temperature: float):
    """Adjust the home's temperature to the specified value in Celsius."""
    return f"Temperature adjusted to {temperature}°C."

@tool
def increase_temperature_by(amount: float):
    """Increase the home's temperature by the specified amount in Celsius."""
    return f"Temperature increased by {amount}°C."




