weight = int(input("ведите массу тела:   "))

gravity = weight * 9.8

print(f"вес тела в ньютонах равен: {gravity:.2f}")

if gravity > 500:
    print("Тело слишком тяжелое")
    
elif gravity < 100:
    print("Слишком легкое")
    
