from math import log, ceil, floor
import argparse


def calc_diff(credit_principal, periods_count, credit_interest):
    if credit_principal < 0 or periods_count < 0 or credit_interest < 0:
        print("Incorrect parameters")
    else:
        interest_rate = credit_interest / 100 / 12
        payments_sum = 0

        for mth in range(1, periods_count + 1):
            mth_diff_payment = ceil(credit_principal / periods_count
                                    + interest_rate
                                    * (credit_principal
                                        - (credit_principal
                                            * (mth - 1) / periods_count)))
            payments_sum += mth_diff_payment
            print(f'Month {mth}: payment is {mth_diff_payment}')

        print()
        print(f'Overpayment = {payments_sum - credit_principal}')


def calc_payment(credit_principal, annuity_payment, credit_interest):
    if credit_principal < 0 or annuity_payment < 0 or credit_interest < 0:
        print("Incorrect parameters")
    else:
        interest_rate = credit_interest / 100 / 12
        periods_count = ceil(log(annuity_payment / (annuity_payment - interest_rate * credit_principal), 1 + interest_rate))
        year_count = periods_count // 12
        month_count = periods_count - 12 * year_count

        if year_count == 0:
            years_str = ""
        elif year_count == 1:
            years_str = "1 year"
        else:
            years_str = f'{year_count} years'

        if month_count == 0:
            month_str = ""
        elif month_count == 1:
            month_str = "1 month"
        else:
            month_str = f'{month_count} months'

        if year_count > 0 and month_count > 0:
            and_str = " and "
        else:
            and_str = ""

        print(f'It will take {years_str}{and_str}{month_str} to repay this credit!')
        print(f'Overpayment = {annuity_payment * periods_count - credit_principal:.0f}')


def calc_annuity(credit_principal, periods_count, credit_interest):
    if credit_principal < 0 or periods_count < 0 or credit_interest < 0:
        print("Incorrect parameters")
    else:
        interest_rate = credit_interest / 100 / 12
        annuity_payment = ceil(credit_principal
                               * (interest_rate * (1 + interest_rate) ** periods_count)
                               / ((1 + interest_rate) ** periods_count - 1))

        print(f'Your annuity payment = {annuity_payment}!')
        print(f'Overpayment = {annuity_payment * periods_count - credit_principal}')


def calc_principal(annuity_payment, periods_count, credit_interest):
    if annuity_payment < 0 or periods_count < 0 or credit_interest < 0:
        print("Incorrect parameters")
    else:
        interest_rate = credit_interest / 100 / 12
        credit_principal = floor(annuity_payment
                                 / ((interest_rate * (1 + interest_rate) ** periods_count)
                                    / ((1 + interest_rate) ** periods_count - 1)))

        print(f'Your credit principal = {credit_principal}!')
        print(f'Overpayment = {annuity_payment * periods_count - credit_principal:.0f}')


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str,
                    help='Enter type of payment: "annuity" or "diff" (differentiated)')
parser.add_argument("--principal", type=int,
                    help="Enter the credit principal")
parser.add_argument("--payment", type=float,
                    help="Enter the monthly payment")
parser.add_argument("--interest", type=float,
                    help="Enter the credit interest")
parser.add_argument("--periods", type=int,
                    help="Enter the number of periods")
args = parser.parse_args()

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        calc_diff(args.principal, args.periods, args.interest)
    else:
        print("Incorrect parameters")

elif args.type == "annuity":
    if args.principal and args.payment and args.interest:
        calc_payment(args.principal, args.payment, args.interest)
    elif args.principal and args.periods and args.interest:
        calc_annuity(args.principal, args.periods, args.interest)
    elif args.payment and args.periods and args.interest:
        calc_principal(args.payment, args.periods, args.interest)
    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")
