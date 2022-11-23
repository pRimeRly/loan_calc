import math
import argparse


def num_monthly_payment(amount_payment, loan_principal, loan_interest):
    a = int(amount_payment)
    loan_p = int(loan_principal)
    i = float(loan_interest)/(12 * 100)
    num_months = math.ceil(math.log((a/(a - i * loan_p)), 1 + i))

    years, months = divmod(num_months, 12)
    text = "It will take "
    text_end = " to repay this loan!"
    if years == 1:
        text = text + f"{years} year"
    if years > 1:
        text = text + f"{years} years"
    if months == 1:
        text = text + f" and {months} month"
    if months > 1:
        text = text + f" and {months} months"
    text = text + text_end
    overpayment = (a * num_months) - loan_p

    print(text)
    print(f"Overpayment = {overpayment}")


def annuity_payment(months, loan_interest, loan_principal):
    loan_p = int(loan_principal)
    n_periods = int(months)
    i = float(loan_interest)/(12 * 100)
    a = math.ceil(loan_p * ((i * math.pow(1 + i, n_periods)) / (math.pow(1 + i, n_periods) - 1)))
    overpayment = (a * n_periods) - loan_p
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {overpayment}")


def calc_loan_principal(amount_payment, months, loan_interest):
    a = int(amount_payment)
    n_periods = int(months)
    i = float(loan_interest)/(12 * 100)
    loan_p = a / ((i * math.pow(1 + i, n_periods))/(math.pow(1 + i, n_periods) - 1))
    overpayment = (a * n_periods) - int(loan_p)
    print(f"Your loan principal = {int(loan_p)}!")
    print(f"Overpayment = {overpayment}")


# Stage 4/4
error_message = "Incorrect parameters"
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()

diff_items = [args.type, args.principal, args.periods, args.interest]
annuity_items = [args.type, args.principal, args.periods, args.interest, args.payment]

annuity_loan_p_items = [args.type,  args.periods, args.interest, args.payment]
annuity_period_items = [args.type, args.principal, args.interest, args.payment]
annuity_payment_items = [args.type, args.principal, args.periods, args.interest]

if args.type not in ["annuity", "diff"]:
    print(error_message)
else:
    if args.type == "diff" and args.payment is not None:
        print(error_message)
    else:
        if args.interest is None:
            print(error_message)
        else:
            if args.type == "diff":
                if diff_items.count(None) != 0:
                    print(error_message)
                else:
                    if float(args.principal) < 0 or float(args.periods) < 0 or float(args.interest) < 0:
                        print(error_message)
                    else:
                        p = int(args.principal)
                        periods = int(args.periods)
                        interest = float(args.interest)/(12 * 100)
                        m = 0
                        all_payments = 0
                        for n in range(1, periods+1):
                            m += 1
                            diff = math.ceil((p / periods) + interest * (p - (p * (m - 1))/periods))
                            all_payments += diff
                            print(f"Month {n}: payment is {diff}")
                        print(f"\nOverpayment = {all_payments - p}")
    if args.interest is None:
        print(error_message)
    else:
        if args.type == "annuity":
            if annuity_items.count(None) != 1:
                print(error_message)
            else:
                if None not in annuity_payment_items:
                    if float(args.principal) <= 0 or float(args.periods) <= 0 or float(args.interest) <= 0:
                        print(error_message)
                    else:
                        principal = args.principal
                        periods = args.periods
                        interest = args.interest
                        annuity_payment(months=periods, loan_interest=interest, loan_principal=principal)
                elif None not in annuity_loan_p_items:
                    if float(args.periods) <= 0 or float(args.interest) <= 0 or float(args.payment) <= 0:
                        print(error_message)
                    else:
                        payment = args.payment
                        periods = args.periods
                        interest = args.interest
                        calc_loan_principal(amount_payment=payment, months=periods, loan_interest=interest)
                elif None not in annuity_period_items:
                    if float(args.principal) <= 0 or float(args.interest) <= 0 or float(args.payment) <= 0:
                        print(error_message)
                    else:
                        principal = args.principal
                        payment = args.payment
                        interest = args.interest
                        num_monthly_payment(amount_payment=payment, loan_interest=interest, loan_principal=principal)
