class Vendor:
    def __init__(self, inventory = None):
        if inventory == None: 
            inventory = []
        self.inventory = inventory

    
    def add(self, item_added):
        self.inventory.append(item_added)
        return item_added
    
    def remove(self, item_removed):
        if item_removed in self.inventory:
            self.inventory.remove(item_removed)
            return item_removed
        else:
            return False

    def get_by_category(self, chosen_category):
        items_in_chosed_category = []
        for item in self.inventory:
            if item.category == chosen_category:
                items_in_chosed_category.append(item)
        return items_in_chosed_category
    
    def swap_items(self, friend, vender_item, friend_item):
        if vender_item in self.inventory and friend_item in friend.inventory:
            self.remove(vender_item)
            self.add(friend_item)
            friend.remove(friend_item)
            friend.add(vender_item)
            return True
        else: 
            return False
    
    def swap_first_item(self, friend):
        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            first_item_vendor = self.inventory[0]
            first_item_friend = friend.inventory[0]
            return self.swap_items(friend, first_item_vendor, first_item_friend)


