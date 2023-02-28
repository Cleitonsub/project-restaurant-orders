from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        foods = []
        for client in self.orders:
            if client[0] == customer:
                foods.append(client[1])
        return Counter(foods).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_foods, foods = set(), set()
        for client in self.orders:
            all_foods.add(client[1])
            if client[0] == customer:
                foods.add(client[1])
        return all_foods.difference(foods)

    def get_days_never_visited_per_customer(self, customer):
        all_days, days = set(), set()
        for client in self.orders:
            all_days.add(client[2])
            if client[0] == customer:
                days.add(client[2])
        return all_days.difference(days)

    def get_busiest_day(self):
        days = []
        for client in self.orders:
            days.append(client[2])
        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        days = []
        for client in self.orders:
            days.append(client[2])
        return Counter(days).most_common()[-1][0]
