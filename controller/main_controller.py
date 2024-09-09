from constant.logger_constant import LOG_APPLICATION_END, LOG_ERROR_CHOICE_RANGE_1_5, LOG_ERROR_ROLE_INTEGER
from constant.menu_constant import MAIN_MENU
from constant.prompt_constant import PROMPT_ROLE
from controller.admin_controller import admin
from controller.customer_controller import customer
from controller.driver_controller import driver
from controller.recycler_controller import recycler
from resources.logger_configuration import logger


def main():
    """
    Displays the main menu and routes the user to the appropriate role-based menu.

    The main menu allows the user to select a role: customer, admin, or exit.
    Logs actions and handles errors related to invalid input.

    Raises:
        ValueError: If the input provided is not a valid integer.
    """
    while True:
        try:
            print(MAIN_MENU)
            role = int(input(PROMPT_ROLE))
            if 1 <= role <= 5:
                if role == 1:
                    customer()
                elif role == 2:
                    admin()
                elif role == 3:
                    driver()
                elif role == 4:
                    recycler()
                elif role == 5:
                    logger.info(LOG_APPLICATION_END)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)
        except ValueError as e:
            logger.error(LOG_ERROR_ROLE_INTEGER, ": ", str(e))


if __name__ == "__main__":
    main()
