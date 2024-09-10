from helper.constant import (
    LOG_RECYCLER_UNAUTHORIZED,
    LOG_ERROR_CHOICE_RANGE_1_3, RECYCLER_MENU, PROMPT_CHOICE, ONE, THREE, TWO,
)

from resources.logger_configuration import logger

from service.recycler import (
    is_recycler_registered,
    get_wastage_report,
    calculate_rate, view_calculated_report
)


def handle_recycling():
    """
      Displays a menu for managing recycler operations and processes user input.

      The function provides four options:
      1. View wastage reports if the recycler is registered.
      2. Calculate and log the recycling rate if the recycler is registered.
      3. Exit the menu.

      Handles invalid input and logs relevant actions and errors. Assumes `RECYCLER_MENU`, `PROMPT_CHOICE`,
      and logging constants are defined elsewhere.
      """
    print(RECYCLER_MENU)
    choice = int(input(PROMPT_CHOICE))
    if ONE <= choice <= THREE:
        if choice == ONE:
            if is_recycler_registered():
                wastage = get_wastage_report()
                for wastage_item, wastage_data in wastage.items():
                    print(wastage_item, " : ", wastage_data)
            else:
                logger.warning(LOG_RECYCLER_UNAUTHORIZED)
        elif choice == TWO:
            if is_recycler_registered():
                wastage_reports = calculate_rate()
                view_calculated_report(wastage_reports)
            else:
                logger.warning(LOG_RECYCLER_UNAUTHORIZED)
    else:
        logger.warning(LOG_ERROR_CHOICE_RANGE_1_3)
