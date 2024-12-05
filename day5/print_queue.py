import os
import re
from read_input import get_input

class SafetyManualUpdate:
    def __init__(self, input_data_path: str):
       self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
       self.input_data = get_input(input_data_path).splitlines() 
       self.number_pattern = re.compile(r'\d+')
       self.update_order = {}
       self.updates = []

    def parse_data(self):
        is_update = False
        
        order_lines = []
        update_lines = []

        for line in self.input_data:
                        
            has_strip_line = line.strip()
            if not has_strip_line:
                is_update = True
                continue

            if not is_update:
                order_lines.append(line)
            else:
                update_lines.append(line)
        
        
        for line in order_lines:
            ops = list(map(int, self.number_pattern.findall(line)))
            if ops[0] not in self.update_order:
                self.update_order[ops[0]] = []
            self.update_order[ops[0]].append(ops[1])

        for line in update_lines:
            self.updates.append(list(map(int, line.split(","))))
       
        
    def is_ordered_update(self, update):
        for page, next_page in zip(update, update[1:]):
            if page not in self.update_order:
                return False
            if next_page not in self.update_order[page]:
               return False
        return True

    def sum_middle_page_number(self):
        self.parse_data()
        middle_pages = []

        for update in self.updates:
            if self.is_ordered_update(update):
                middle_pages.append(update[len(update) // 2])
            
        return sum(middle_pages)

    def sum_middle_page_number_new(self):
        self.parse_data()
        middle_pages_ordered = []

        for update in self.updates:
            if not self.is_ordered_update(update):
                new_update = self.order_update(update)
                middle_pages_ordered.append(new_update[len(new_update) // 2])

        return sum(middle_pages_ordered)


    # part 2

    def order_update(self, update):
        
        not_keys = []
        temp_update = []
        
        for page in update:
            if page not in list(self.update_order):
                not_keys.append(page)
            else:
                temp_update.append(page)
        
        update = list(temp_update + not_keys)
        
        new_update = []
        for page in update:
            insert_pos = 0
            flag = False
            if len(new_update) == 0:
                new_update.append(page)
            else:
                for inserted_page in new_update:
                    if inserted_page not in self.update_order or page in self.update_order[inserted_page]:
                        insert_pos += 1
                    else:
                        flag = True
                        new_update.insert(insert_pos, page)
                        break

                if not flag:
                    new_update.insert(insert_pos, page)
        
        return new_update

