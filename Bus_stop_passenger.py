def number(bus_stops):
    InBus = 0
    for i in bus_stops:
        InBus += i[0] - i[1]
    return InBus