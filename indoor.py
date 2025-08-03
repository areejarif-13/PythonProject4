def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   n=d.replace('$',"")

   m=float(n)
   return m


def percent_to_float(p):

    n1=p.replace("%","")
    n=float(n1)
    n=n/100
    return n
main()
