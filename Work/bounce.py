# bounce.py
#
# Exercise 1.5
REBOUND = 0.6


if __name__ == "__main__":
    height = 100.0
    num_bounces = 10
    for i in range(num_bounces):
        height *= REBOUND
        print(f"{i + 1} {round(height, 4)}")
