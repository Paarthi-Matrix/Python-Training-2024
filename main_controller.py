from controller.admin import manage_admin_tasks
from controller.customer import perform_customer_actions, ask_for_continue
from controller.driver import perform_driver_actions
from controller.recycler import handle_recycling
from exception.custom_exception import ExceedLimitException, UserAlreadyExistsError, ResourceNotFoundException, \
    GarbageCollectorException, ResourceAlreadyExistsException
from helper.constant import (LOG_APPLICATION_END,
                             LOG_ERROR_CHOICE_RANGE_1_5,
                             MAIN_MENU, PROMPT_ROLE, LOG_VALUE_ERROR_IN_CUSTOMER_MENU,
                             PROMPT_CONTINUE_PROCESS, PROMPT_YES, ONE, FIVE, TWO, THREE, FOUR)
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
            if ONE <= role <= FIVE:
                if role == ONE:
                    data = perform_customer_actions()
                    if 'status' in data:
                        print(data['status'])
                    if 'work_reports' in data:
                        for work_item, work_detail in data['work_reports'].items():
                            print(work_item, " : ", work_detail)
                    if 'customer_id' in data:
                        print("Customer Id: ", data['customer_id'])
                        for customer_item, customer_detail in data['customer_details'].items():
                            if customer_item != "password":
                                print(customer_item, " : ", customer_detail)
                    if 'bin_id' in data:
                        print("Bin_Id: ", data['bin_id'])
                        for bin_item, bin_detail in data['bin_details'].items():
                            if bin_item != "customer_id":
                                print(bin_item, " : ", bin_detail)
                elif role == TWO:
                    manage_admin_tasks()
                elif role == THREE:
                    perform_driver_actions()
                elif role == FOUR:
                    handle_recycling()
                elif role == FIVE:
                    logger.info(LOG_APPLICATION_END)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_5)
        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_CUSTOMER_MENU.format(e=e))
        except UserAlreadyExistsError as e:
            logger.error(e)
        except ResourceNotFoundException as e:
            logger.error(e)
        except GarbageCollectorException as e:
            logger.error(e)
        except ExceedLimitException as e:
            logger.warning(e)
        except ResourceAlreadyExistsException as e:
            logger.warning(e)


if __name__ == "__main__":
    main()
