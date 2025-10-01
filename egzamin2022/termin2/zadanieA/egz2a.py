from egz2atesty import runtests
class SegmentTree:
    def __init__(self, size, capacity):
        """
        Inicjalizuje drzewo segmentowe o co najmniej `size` magazynach,
        z których każdy ma początkowo pojemność `capacity`.
        """
        self.N = 1
        while self.N < size:
            self.N *= 2  # ustalamy rozmiar jako potęgę dwójki
        self.capacity = capacity
        self.tree = [capacity] * (2 * self.N)  # pełna tablica drzewa segmentowego

    def update(self, index, value):
        """
        Aktualizuje stan magazynu `index`, zmniejszając jego wolną pojemność o `value`.
        Następnie aktualizuje wszystkie węzły nadrzędne w drzewie.
        """
        i = index + self.N  # przechodzimy do liścia reprezentującego magazyn
        self.tree[i] -= value  # zmniejszamy wolną pojemność
        i //= 2
        while i >= 1:
            # Aktualizujemy wartość węzła nadrzędnego jako maksimum z dzieci
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def query(self, weight):
        """
        Znajduje najmniejszy indeks magazynu, który pomieści `weight` ton węgla.
        Jeśli żaden magazyn nie ma wystarczająco miejsca, zwraca -1.
        """
        if self.tree[1] < weight:
            return -1  # żaden magazyn nie ma wystarczająco miejsca
        i = 1  # zaczynamy od korzenia
        while i < self.N:
            # Schodzimy do dziecka, które może pomieścić transport
            if self.tree[2 * i] >= weight:
                i = 2 * i  # lewe dziecko
            else:
                i = 2 * i + 1  # prawe dziecko
        return i - self.N  # liść odpowiadający indeksowi magazynu


def coal(A, T):
    """
    Funkcja główna.
    Przyjmuje listę A z ilościami węgla i T - pojemność każdego magazynu.
    Zwraca numer magazynu, w którym umieszczono ostatni transport.
    """
    n = len(A)
    MAX_WAREHOUSES = 2 * n  # przyjmujemy bezpieczny zapas magazynów
    st = SegmentTree(MAX_WAREHOUSES, T)  # tworzymy drzewo segmentowe
    last_used = 0  # numer magazynu, do którego trafił ostatni transport

    for coal_tons in A:
        idx = st.query(coal_tons)  # znajdź najniższy możliwy magazyn
        if idx == -1:
            raise Exception("Nie znaleziono magazynu — nie powinno się zdarzyć, magazynów jest dużo")
        st.update(idx, coal_tons)  # zaktualizuj pojemność magazynu
        last_used = idx  # zapamiętaj numer ostatniego magazynu

    return last_used  # zwróć numer magazynu dla ostatniego transportu

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = False )
