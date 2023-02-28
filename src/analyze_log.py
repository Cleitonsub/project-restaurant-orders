import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r", encoding="utf-8") as file:
            content = list(csv.reader(file))
        analyze_csv_list(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def write_in_csv_format(
        maria_eats,
        arnaldo_ask_hamburguer,
        orders,
        days):
    maria_most_ordered = None
    maria_most_ordered_times = 0

    for order in maria_eats:
        if maria_eats[order] > maria_most_ordered_times:
            maria_most_ordered = order
            maria_most_ordered_times = maria_eats[order]
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(f"{maria_most_ordered}\n")
        file.writelines(f"{str(arnaldo_ask_hamburguer)}\n")
        file.writelines(f"{str(orders)}\n")
        file.writelines(f"{str(days)}")
        file.close()


def add_maria_eats(maria_eats, order):
    if order not in maria_eats:
        maria_eats[order] = 1
    else:
        maria_eats[order] += 1


def joao_data(joao_never_ask, order, day, joao_never_went):
    joao_never_ask.add(order)
    if day != "domingo":
        joao_never_went.add(day)


def analyze_csv_list(csv_list):
    maria_eats = {}
    arnaldo_ask_hamburguer = 0
    orders, joao_never_ask, days, joao_never_went = set(), set(), set(), set()

    for customer, order, day in csv_list:
        if customer == "maria":
            add_maria_eats(maria_eats, order)

        if customer == "arnaldo" and order == "hamburguer":
            arnaldo_ask_hamburguer += 1

        if customer == "joao":
            joao_data(joao_never_ask, order, day, joao_never_went)

        days.add(day) if day != "domingo" else None
        orders.add(order)

    write_in_csv_format(
        maria_eats,
        arnaldo_ask_hamburguer,
        orders.difference(joao_never_ask),
        days.difference(joao_never_went)
    )
# Inspirado no nosso amigo Rafael Moraes
