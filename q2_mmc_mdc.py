def mdc(num1, num2):
    i = 1
    while (i <= num1 and i <= num2):
        if (num1 % i == 0 and num2 % i == 0):
            mdc = i
        i += 1
    return mdc

def mmc(num1, num2):
    mmc = (num1 * num2) / mdc(num1, num2)
    return mmc

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"O MDC entre {num1} e {num2} é: {mdc(num1, num2)}")
print(f"O MMC entre {num1} e {num2} é: {mmc(num1, num2)}")