def get_line_log(user_id, bool_obj, label):
    return f"User - {user_id} {'has' if bool_obj else 'has not'} {label}."
