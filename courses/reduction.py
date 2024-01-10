def discount(numbers):
    for number in range(len(numbers)):
        numbers[number] = numbers[number].replace("€","")
        discouted_price = float(numbers[number]) * 0.75
        numbers[number] = f"{discouted_price:.2f}€" 
    #print (numbers)
    return numbers




prices = ["24.75€", "55.66€", "89.20€"]
princes_discounted = discount(prices)
print (princes_discounted)