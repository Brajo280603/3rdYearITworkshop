def number_to_words(n):

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    if n == 0:
        return "Zero"
    
    def three_digit_to_words(num):

        word = ""
        if num // 100 > 0:
            word += ones[num // 100] + " Hundred "
        num %= 100
        if 10 < num < 20:
            word += teens[num - 10] + " "
        else:
            if num // 10 > 0:
                word += tens[num // 10] + " "
            num %= 10
            if num > 0:
                word += ones[num] + " "
        return word.strip()
    
    word = ""
    part = 0
    while n > 0:
        if n % 1000 != 0:
            word = three_digit_to_words(n % 1000) + " " + thousands[part] + " " + word
        n //= 1000
        part += 1
    
    return word.strip()

number = int(input("Enter a number : "))
print(number_to_words(number))  
