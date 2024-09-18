import uuid

from constant.constant import (POOL_THRESHOLD, MSG_POOL_CREATION, POOL_BALANCE, ERROR_POOL_BALANCE,
                               USER_CONTRIBUTION_SUCCESS, ERROR_POOL_CONTRIBUTION,
                               USER_NOT_FOUND)

from service.user import users_db

from resources.log_configuration import setup_logger

logger = setup_logger()

pools = {}
current_pool_id = None


def create_new():
    """Create a new pool.
    - New pool which collects the amount is created.
    - Once reaches threshold automatically new pool is created
    - """
    global current_pool_id
    pool_id = f"pool_{str(uuid.uuid4())}"
    pools[pool_id] = {
        "current_pool": [],
        "total_funds": 0
    }
    current_pool_id = pool_id
    logger.info(MSG_POOL_CREATION.format(pool_id))


def contribute_current(user_id, amount):
    """
    Contribution of amount to pool
    - User enters the user_id
    - user_id is checked if the user is available
    - amount is entered as float
    :param user_id: User_id generated uuid
    :param amount: amount is float value entered by user
    :return: True or False
    """
    global current_pool_id
    if user_id in users_db:
        if users_db[user_id]["amount"] > amount:
            if (current_pool_id is None) or (pools[current_pool_id]["total_funds"] > POOL_THRESHOLD):
                create_new()
            pools[current_pool_id]["current_pool"].append((user_id, amount))
            pools[current_pool_id]["total_funds"] += amount
            users_db[user_id]["amount"] -= amount
            logger.info(USER_CONTRIBUTION_SUCCESS.format(user_id, amount))
            return True
        else:
            logger.error(ERROR_POOL_CONTRIBUTION.format(user_id))
            return False
    else:
        logger.error(USER_NOT_FOUND)
        return False


def get_pool_balance():
    """
    Checks for the pool balance
    - Pool balance is displayed.
    - Total amount of contribution
    :return: Balance float type is used.
    """
    if current_pool_id in pools:
        balance = pools[current_pool_id]["total_funds"]
        logger.info(POOL_BALANCE.format(balance))
        return balance
    else:
        logger.error(ERROR_POOL_BALANCE)
        return None
