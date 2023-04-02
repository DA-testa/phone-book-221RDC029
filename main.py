# python3
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

class phone_book:
    def __init__(self):
        self.contacts = {}

    def pievieno(self, number, name):
        self.contacts[number] = name

    def atrod(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "person is not found"

    def izdzēst(self, number):
        if number in self.contacts:
            del self.contacts[number]
            return True
        else:
            return False
    
def process_queries(queries):
    result = []
    kontaktu_grāmata = phone_book()
    for cur_query in queries:
        if cur_query.type == 'add':
            kontaktu_grāmata.pievieno(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            kontaktu_grāmata.izdzēst(cur_query.number)
        else:
            numurs = cur_query.number
            atrast_numuru = kontaktu_grāmata.atrod(numurs)
            result.append(atrast_numuru)
    return result

if __name__ == '__main__':
   write_responses(process_queries(read_queries()))