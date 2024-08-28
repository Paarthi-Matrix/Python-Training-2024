import uuid

admin_detail = {}


def register_admin(name, email, password):
    if len(admin_detail) > 1:
        return None
    else:
        admin_id = str(uuid.uuid4())
        admin_detail["admin_id"] = admin_id
        admin_detail["name"] = name
        admin_detail["email"] = email
        admin_detail["password"] = password
