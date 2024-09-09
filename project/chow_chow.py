from common.common_constants import (
    PICK_CHOICE, EXITING,
    INVALID_CHOICE,
    INVALID_INPUT, AUTHORIZATION, ZERO, ONE, TWO,
    THREE
)
from controller.customer_controller import customer_operations
from controller.delivery_person_controller import delivery_person_operations
from controller.restaurant_controller import restaurant_operations
from resources.logging_config import logger

def chow_now():
    """
    Main function to start the application and handle role selection.

    This function allows the user to pick a role (customer or restaurant)
    and then directs them to the appropriate set of operations.
    The function continues to loop until the user decides to exit the application.
    """
    while True:
        try:
            print(AUTHORIZATION)
            choice = input(PICK_CHOICE)
            if not (choice.isnumeric()
                    and len(choice) == ONE and ZERO <= int(choice) <= THREE):
                raise ValueError
            choice = int(choice)
            if choice == ONE:
                customer_operations()
            elif choice == TWO:
                restaurant_operations()
            elif choice == THREE:
                delivery_person_operations()
            elif choice == ZERO:
                logger.debug(EXITING)
                break
            else:
                logger.warning(INVALID_CHOICE)
        except ValueError:
            logger.error(INVALID_INPUT)


if __name__ == "__main__":
    chow_now()
