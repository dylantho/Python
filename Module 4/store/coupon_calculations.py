def calculate_price(originalPrice, cash_coupon, percent_coupon):
    #setup
    if originalPrice < 10:
        shippingRate = 5.95
    elif 10 <= originalPrice <30:
        shippingRate = 7.95
    elif 30 <= originalPrice <50:
        shippingRate = 11.95
    elif originalPrice >= 50:
        shippingRate = 0
    taxRate = .06
    percentActual = 1 - percent_coupon

    #math
    midPrice = (originalPrice - cash_coupon) * percentActual
    taxCost = midPrice * taxRate
    endPrice = midPrice + taxCost + shippingRate

    return endPrice


if __name__ == '__main__':
    originalPrice = float(input("Enter the original price: "))
    cash_coupon = float(input("Enter the cash coupon you have: "))
    percent_coupon = float(input("Enter the percent off coupon amount: "))
    endPrice = calculate_price(originalPrice, cash_coupon, percent_coupon)
    print(endPrice)
