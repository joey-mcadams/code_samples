inputString = "US:UK:FedEx:5,UK:US:UPS:4,UK:CA:FedEx:7,US:CA:DHL:10,UK:FR:DHL:2"


def shippingCost(input_string: str, source_country: str, target_country: str, method: str) -> int:
    shipping_dict = create_shipping_dictionary(input_string)

    sources = shipping_dict.get(source_country)
    if sources is None:
        raise Exception("Source country not found")

    for shipping_method in sources:
        if shipping_method.get("destination") == target_country and shipping_method.get("method") == method:
            return shipping_method.get("cost")

    raise Exception("Could not find shipping method that matched input parameters.")


def create_shipping_dictionary(input_string):
    types_of_shipping = input_string.split(",")
    shipping_dict = {}
    for shipping_type in types_of_shipping:
        entries = shipping_type.split(":")
        if not entries[0] in shipping_dict.keys():
            shipping_dict[entries[0]] = []

        shipping_dict[entries[0]].append({"destination": entries[1],
                                          "method": entries[2],
                                          "cost": entries[3]})
    return shipping_dict


def shippingRoute(input_string, source_country, target_country):
    shipping_dict = create_shipping_dictionary(input_string)

    possible_first_stops = shipping_dict.get(source_country)

    if possible_first_stops is None:
        raise Exception("Source country not found")

    second_stops = []

    for second_stop in possible_first_stops:
        destination = second_stop.get("destination")
        method = second_stop.get("method")
        cost = second_stop.get("cost")

        # If one hop.
        if destination == target_country:
            return {
                "route": f"{source_country} -> {target_country}",
                "method": method,
                "cost": cost
            }

        second_stops.append(second_stop)

    for possible_destination in second_stops:
        end_destinations = shipping_dict.get(possible_destination.get("destination"))
        for end_destination in end_destinations:
            if end_destination.get("destination") == target_country:
                return {
                    "route": f"{source_country} -> {possible_destination.get("destination")} -> {target_country}",
                    "cost": int(possible_destination.get("cost")) + int(end_destination.get("cost")),
                    "method": f"{possible_destination.get("method")} -> {end_destination.get("method")}"
                }

    raise Exception("Could not find shipping method that matched input parameters.")


print(shippingRoute(inputString, "US", "FR"))

# print(shippingCost(inputString, "US", "UK", "FedEx"))
# print(shippingCost(inputString, "UK", "FR", "DHL"))

# print(shippingCost(inputString, "DE", "FR", "DHL"))
# print(shippingCost(inputString, "UK", "DE", "DHL"))
