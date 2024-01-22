class Moon:
    def __init__(self, name="New Moon", risk_level="D", conditions="", fauna="Unknown.", price=0):
        self.name = name
        self.risk_level = risk_level
        self.conditions = conditions
        self.fauna = fauna
        self.price = price
        self.description = f"RISK LEVEL: {self.risk_level}\nPRICE: {self.price}\nCONDITIONS: {self.conditions}\nFAUNA: {self.fauna}"


if __name__ == "__main__": 
    moon1 = Moon("Experimentation", "B", 
             "Arid. Low habitability, worsened by industrial artifacts."\
             , "Unknown.")

    print()
    print(moon1.name)
    print(moon1.description)
    print()