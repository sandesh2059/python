# name = ['Jaaannne', 'Maaarrk', 'Alleeexx']
# result = []

# for word in name:
#     unique = ''
#     for ch in word:
#         if ch not in unique:
#             unique += ch
#     result.append(unique)
# print(result)



class data_cleaner:

    def __init__(self, names):
        self.names = names

    def remove_duplicates(self):
        result = []

        for word in self.names:
            unique = ''
            for ch in word:
                if ch not in unique:
                    unique += ch
            result.append(unique)
        return result
    
    def show_updated_list(self):
        cleaned = self.remove_duplicates()
        print(cleaned)
    
names = ['Jaaannne', 'Maaarrk', 'Alleeexx']

obj1 = data_cleaner(names)
obj1.show_updated_list()
