class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        bigUnits = ["Thousand", "Million", "Billion"]
        result = self.threeDigits(num % 1000)
        num //= 1000
        
        for i in range(len(bigUnits)):
            if num > 0 and num % 1000 > 0:
                result = self.threeDigits(num % 1000) + bigUnits[i] + " " + result
            num //= 1000
        
        return result.strip()

    def threeDigits(self, num: int) -> str:
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        result = ""
        if num > 99:
            result += ones[num // 100] + " Hundred "
        
        num %= 100
        if num < 20 and num > 9:
            result += teens[num - 10] + " "
        else:
            if num >= 20:
                result += tens[num // 10] + " "
            num %= 10
            if num > 0:
                result += ones[num] + " "
        
        return result
