def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    
    if n == 0:
        return "Zero"
    
    result = ""
    part = 0      
    while n > 0:
        num = n % 1000
        n //= 1000
        
        if num != 0:
            group_words = ""
            if num // 100 > 0:
                group_words += ones[num // 100] + " Hundred "
            num %= 100
            if 10 < num < 20:
                group_words += teens[num - 10] + " "
            else:
                if num // 10 > 0:
                    group_words += tens[num // 10] + " "
                num %= 10
                if num > 0:
                    group_words += ones[num] + " "
            
            result = group_words.strip() + " " + thousands[part] + " " + result
        
        part += 1      
    return result.strip()

number = int(input("Enter a number : "))
print(number_to_words(number))  
