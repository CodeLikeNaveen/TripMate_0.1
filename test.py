from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent




# res = tavily_search("Best hotels in india")


# res = search_flights("Plan a 7 days Japan trip from India")

# print(res)

user_input = input("Enter a travel request")
# Plan a complete 7 days Nepal trip from India including flights, hotels and sightseeing under 2 lakhs.

res = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
    )

print("\nFinal Response")
print(res["answer"])