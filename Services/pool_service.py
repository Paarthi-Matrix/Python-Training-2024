import uuid


from Utils.constants import (POOL_THRESHOLD, MSG_POOL_CREATION, POOL_BALANCE, ERROR_POOL_BALANCE,
                             USER_CONTRIBUTION_SUCCESS, ERROR_POOL_CONTRIBUTION, USER_CONTRIBUTION_FAILURE,
                             USER_NOT_FOUND)
from Utils.log_configuration import setup_logger

logger = setup_logger()

pools = {}
current_pool_id = None


def create_new_pool():
    """Create a new pool."""
    global current_pool_id
    pool_id = f"pool_{str(uuid.uuid4())}"
    pools[pool_id] = {
        "current_pool": [],
        "total_funds": 0
    }
    current_pool_id = pool_id
    logger.info(MSG_POOL_CREATION.format(pool_id))


def contribute(user_id, amount, pools, users_db):
    global current_pool_id
    try:
        if user_id in users_db:
            if users_db[user_id]["amount"] > amount:
                if (current_pool_id is None) or (pools[current_pool_id]["total_funds"] > POOL_THRESHOLD):
                    create_new_pool()
                pools[current_pool_id]["current_pool"].append((user_id, amount))
                pools[current_pool_id]["total_funds"] += amount
                users_db[user_id]["amount"] -= amount
                logger.info(USER_CONTRIBUTION_SUCCESS.format(user_id, amount))
                return True
            else:
                logger.error(USER_CONTRIBUTION_FAILURE.format(user_id))
                return False
        else:
            logger.error(USER_NOT_FOUND)
            return False
    except ValueError:
        logger.error(ERROR_POOL_CONTRIBUTION)
        return False


def get_pool_balance():
    try:
        if current_pool_id in pools:
            balance = pools[current_pool_id]["total_funds"]
            logger.info(POOL_BALANCE.format(balance))
            return balance
        else:
            logger.error(ERROR_POOL_BALANCE)
            return None
    except ValueError:
        logger.error(ERROR_POOL_BALANCE)
        return None
