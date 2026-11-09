def shutdown(Y):
    """
    Shutdown
    """
    if Y == "yes":
        print("Shutting down...")
        # Add shutdown logic here
    elif Y == "no":
        print("Shutdown Aborted.")

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

Y = input("Do you want to shutdown? (yes/no): ").lower()
shutdown(Y)