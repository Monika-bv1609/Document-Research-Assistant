from app.tools.web_search import (
    search_web
)

from app.tools.weather import (
    get_weather
)

from app.tools.current_time import (
    get_current_time
)

from app.tools.calculator import (
    calculate_expression
)

# Tool registry
TOOLS = {

    "web_search":
    search_web,

    "weather":
    get_weather,

    "time":
    get_current_time,

    "calculator":
    calculate_expression
}