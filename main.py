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

# Kad tiks ievadīta jauna kontaktpersona un tā nebūs atrasta jau dotajās kontaktpersonās, tad tiks izsaukta šī
# metode, kura saglabās telefona numuru un vārdu attiecīgos mainīgos, kas ir number un name, tāpēc arī tiek piešķirts self
class phone_book:
    def __init__(self, number, name):
        self.number = number
        self.name = name

def process_queries(queries):
    result = []
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # Izveidoju mainīgo atrasts, lai ietu caur kontaktu lsitu un pārbaudītu jau esošos kontaktus
            # un uzzinātu, vai tiek atrasta meklētā persona.
            atrasts = False
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    # Ja persona tiek atrasta, tad mainīgais atrasts nomainās uz true, un ciklst turpinās
                    atrasts = True
                    # Ja persona nav atrasta, tad tā tiks pievienota kontaktos caur phone_book metodi, kura tika izvediota
                    # iepriekš
                    if not atrasts:
                        jauns_kontakts = phone_book(cur_query.number, cur_query.name)
                        contacts.append(jauns_kontakts)
                    break
            else:
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