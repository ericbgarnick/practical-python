SEARS_HEIGHT_INCHES = 1729 * 12
BILL_THICKNESS_INCHES = 0.0043

SEARS_HEIGHT_METERS = 442
BILL_THICKNESS_METERS = 0.11 * 0.001


def sears_dollars(num_days: int, num_bills: int):
    bill_height = num_bills * BILL_THICKNESS_METERS

    if bill_height > SEARS_HEIGHT_METERS:
        print(f"Over Sears Tower in {num_days} days")
    else:
        sears_dollars(num_days + 1, num_bills * 2)


if __name__ == "__main__":
    sears_dollars(1, 1)
