from guitar import Guitar

def main():
    """Test the Guitar class."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000)

    # Test get_age method
    print("Gibson L-5 CES get_age() - Expected 100. Got", guitar1.get_age())
    print("Another Guitar get_age() - Expected 9. Got", guitar2.get_age())

    # Test is_vintage method
    print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got", guitar2.is_vintage())

if __name__ == "__main__":
    main()