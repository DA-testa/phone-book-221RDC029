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

# Kad tiks ievadīta jauna kontaktpersona, tad tiks izsaukta šī metode, kura saglabās telefona
# numuru un vārdu attiecīgos mainīgos, kas ir number un name.
class phone_book:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            # Izveido mainīgo atrasts, lai zinātu, vai tiek atrasta meklētā persona
            atrasts = False
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    atrasts = True
                    # Ja persona nav atrasta, tad tā tiks pievienota kontaktos
                    if not atrasts:
                        jauns_kontakts = phone_book(cur_query.number, cur_query.name)
                        contacts.append(jauns_kontakts)
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))