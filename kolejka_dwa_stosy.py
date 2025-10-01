#kolejka zaimplementowana dzieki 2 stos
inn=[]
outt=[]
def put(el):
    inn.append(el)
def get(el):
    if not outt: #jak outt pusty
        while inn:
            outt.append(inn.pop())
    return outt.pop()
