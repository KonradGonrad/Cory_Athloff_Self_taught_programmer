class PublicPrivateExample:
    def __init__(self):
        self.public = "bezpieczny"
        self.private = "niebezpieczny"
    
    def public_method(self):
        #można odwołać się do tej komendy
        print("Tak")
        pass

    def _unsafe_method(self):
        #ta metoda nie powinna być używana poza klasą
        print("Nie")
        pass

public_private = PublicPrivateExample()
public_private.public_method()
public_private._unsafe_method()
