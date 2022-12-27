def filter_by_gen(id: int = None, **filters) -> dict:
    filter_by = dict(id=id)
    if id is None:
        filter_by = {**filters}
    return filter_by
