def truncate_name(name, max_length=30):
    if len(name) > max_length:
        return name[:max_length - 3] + '...'
    return name
            