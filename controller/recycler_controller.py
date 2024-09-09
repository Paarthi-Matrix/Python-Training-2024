from constant.logger_constant import (
    LOG_VALUE_ERROR_IN_ADMIN_MENU,
    LOG_REDIRECTING_HOME,
    LOG_RECYCLER_UNAUTHORIZED,
    LOG_RATE_CALCULATED,
    LOG_ERROR_CHOICE_RANGE_1_3,
)

from constant.menu_constant import (
    RECYCLER_MENU
)

from constant.prompt_constant import (
    PROMPT_CHOICE
)

from resources.logger_configuration import logger


from service.recycler_service import (
    is_recycler_registered,
    get_wastage_report,
    calculate_rate, get_calculated_report, view_calculated_report
)

from exception.custom_exception import (
    ResourceNotFoundException, GarbageCollectorException
)


def recycler():
    """
      Displays a menu for managing recycler operations and processes user input.

      The function provides four options:
      1. View wastage reports if the recycler is registered.
      2. Calculate and log the recycling rate if the recycler is registered.
      3. Exit the menu.

      Handles invalid input and logs relevant actions and errors. Assumes `RECYCLER_MENU`, `PROMPT_CHOICE`,
      and logging constants are defined elsewhere.
      """
    while True:
        try:
            print(RECYCLER_MENU)
            choice = int(input(PROMPT_CHOICE))
            if 1 <= choice <= 3:
                if choice == 1:
                    if is_recycler_registered():
                        wastage = get_wastage_report()
                        for wastage_item, wastage_data in wastage.items():
                            print(wastage_item, " : ", wastage_data)
                    else:
                        logger.warning(LOG_RECYCLER_UNAUTHORIZED)
                elif choice == 2:
                    if is_recycler_registered():
                        wastage_reports = calculate_rate()
                        view_calculated_report(wastage_reports)
                    else:
                        logger.warning(LOG_RECYCLER_UNAUTHORIZED)
                elif choice == 3:
                    logger.info(LOG_REDIRECTING_HOME)
                    break
            else:
                logger.warning(LOG_ERROR_CHOICE_RANGE_1_3)
        except ValueError as e:
            logger.error(LOG_VALUE_ERROR_IN_ADMIN_MENU.format(e=e))
        except ResourceNotFoundException as e:
            logger.error(e)
        except GarbageCollectorException as e:
            logger.error(e)
