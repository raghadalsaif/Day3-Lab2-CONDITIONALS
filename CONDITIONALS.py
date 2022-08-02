movieName = "over the moon"
rating = 3
scoreofpopularity = 72.65


if rating == 4 and scoreofpopularity > 80:
    print("Highly recommended")
elif rating == 3 or rating > 3 and scoreofpopularity > 70:
    print("I recommended it . It is good")
elif rating == 2 or rating < 2 and scoreofpopularity > 50:
    print("Don't watch it. It is a waste of time")

