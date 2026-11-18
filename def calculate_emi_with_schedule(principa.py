def calculate_emi_with_schedule(principal, annual_rate, years):
    # Convert annual interest rate to a monthly decimal
    monthly_rate = (annual_rate / 100) / 12
    months = years * 12
    
    # Standard EMI Formula
    emi = principal * monthly_rate * ((1 + monthly_rate)**months) / (((1 + monthly_rate)**months) - 1)
    total_payment = emi * months
    total_interest = total_payment - principal
    
    print("--- Loan Summary ---")
    print(f"Principal Amount : ₹{principal:,.2f}")
    print(f"Interest Rate    : {annual_rate}% p.a.")
    print(f"Tenure           : {years} years ({months} months)")
    print(f"Monthly EMI      : ₹{emi:,.2f}")
    print(f"Total Interest   : ₹{total_interest:,.2f}\n")
    
    print("--- Repayment Schedule (Month by Month) ---")
    print(f"{'Month':<6} | {'EMI':<12} | {'Principal':<12} | {'Interest':<12} | {'Balance':<12}")
    print("-" * 65)
    
    balance = principal
    for month in range(1, months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = emi - interest_payment
        balance -= principal_payment
        
        # Prevent negative balance due to rounding
        if balance < 0:
            balance = 0
            
        print(f"{month:<6} | ₹{emi:<10,.2f} | ₹{principal_payment:<10,.2f} | ₹{interest_payment:<10,.2f} | ₹{balance:<10,.2f}")

# Run the updated calculator
calculate_emi_with_schedule(principal=500000, annual_rate=8.5, years=2)