# ============================================================
# Self-Assessment
#
# 1. My first debugging step was to read the error message and
#    check the code around the line where the error occurred.
#    I learned that debugging requires checking the code
#    carefully and understanding what each line does.
#
# 2. apply_discount(price, tier) takes a price and a customer
#    membership tier as inputs. It applies a discount based on
#    the tier and returns the discounted price. Gold receives
#    15%, silver receives 10%, bronze receives 5%, and any
#    other tier receives no discount. A colleague could use
#    the function by providing a price and a tier.
#
# 3. AI disclosure: I used ChatGPT to help understand the
#    assignment requirements and organize the Python functions.
#    I reviewed the code to understand how the functions work.
# ============================================================


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")

tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After tax: ${total:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(
    f'final_price(200, "gold", 0.07) = '
    f"${final_price(200, 'gold', 0.07):.2f}"
)


# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(
        f"Price: ${price:.2f} | "
        f"Tier: {tier} | "
        f"Final: ${total:.2f}"
    )


# --- Exercise 6 ---

x = 100  # Global variable


def double_it():
    x = 999  # Local variable; separate from the global x
    return x * 2


print(x)            # Prints 100
print(double_it())  # Prints 1998
print(x)            # Prints 100 again

# Scope explanation:
# A local variable exists inside its function, while a global
# variable is defined outside functions. The x inside
# double_it() is local, so changing or assigning it does not
# change the global x.