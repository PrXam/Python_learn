import operator
import json


class Item:

    def __init__(self, item_id, count, return_count, status):
        self.item_id = item_id
        self.count = count
        self.return_count = return_count
        self.status = status


class Order:

    def __init__(self, order_id):
        self.order_id = order_id
        self.items = {}

    def item_in_order(self, kwargs):
        item = Item (kwargs["item_id"], kwargs["count"], kwargs["return_count"], kwargs["status"])
        self.items[kwargs["item_id"]] = item

    def return_order(self):
        item_list = []
        for item in self.items.keys():
            if self.items[item].status == "OK" and (self.items[item].count - self.items[item].return_count)>0:
                dict_item = {"count":(self.items[item].count - self.items[item].return_count),"id":self.items[item].item_id}
                item_list.append(dict_item)
        return item_list


def input_event():
    with open("input.txt", "r") as f:
        list_event = (json.load(f))
    dict_order = {}
    for event in sorted(list_event, key=lambda x: x["event_id"]):
        order_id = event["order_id"]
        if order_id not in dict_order.keys():
            order = Order(order_id)
            dict_order[order_id] = order
        dict_order[order_id].item_in_order(event)
    return dict_order


def output_order(dict_order):
    output = []
    for order in dict_order.keys():
        items = dict_order[order].return_order()
        if items:
            order_dict = {"id": dict_order[order].order_id, "items": items}
            output.append(order_dict)
    print(json.dumps(output))


dict_order = input_event()
output_order(dict_order)
