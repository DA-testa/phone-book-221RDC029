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

# Izveidoju jaunu klasi phone_book, kur saglabāšu savas vērtības un veikšu risinājumus
# lai prasītās vērtības atrastu
class phone_book:
    def __init__(self):
        self.contacts = {}

    # Šajā metodē tiks veikta telefona numura un vārda pievienošana telefona grāmatai
    def pievieno(self, number, name):
        self.contacts[number] = name

    # Šajā metodē tiks veikta telefona vārda atrašana, pēc ievadītā numura
    # Ja tāds numurs eksistē, tad tiks izvadīts tās personas vārds, kuram pieder šis telefona numurs
    # Ja neeksistē, tad tiks izvadīts "not found"
    def atrod(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "not found"

    # Šajā metodē tiks veikta personas vārda dzēšana
    # Ja telefona ievadītais telefona numurs eksistē telefona grāmatā, tad vārds tiek izdzēsts
    # Ja neeksistē, tad vienkārši dod atpakaļ False un nekas nenotiek
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
        # Ja ievadītais vārds ir "add", tad izsauc pievienošanas metodi
        if cur_query.type == 'add':
            kontaktu_grāmata.pievieno(cur_query.number, cur_query.name)
        # Ja ievadītasis vārds sākumā ir "del", tad izsauc dzēšanas metodi
        elif cur_query.type == 'del':
            kontaktu_grāmata.izdzēst(cur_query.number)
        else:
        # Trešā metode, kura paliek pāri ir atrast numuru, tāpēc, ja tiks ievadīts "find", tad tiks izsaukta metode
        # atrod un tiks izvadīts prasītais vārds
            numurs = cur_query.number
            atrast_numuru = kontaktu_grāmata.atrod(numurs)
            result.append(atrast_numuru)
    return result

if __name__ == '__main__':
   write_responses(process_queries(read_queries()))