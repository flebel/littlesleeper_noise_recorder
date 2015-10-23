from sqlalchemy.orm.exc import NoResultFound


def get_or_create(session, model, create_method='', create_method_kwargs=None, **kwargs):
    """
    http://stackoverflow.com/a/21146492
    """
    try:
        return session.query(model).filter_by(**kwargs).one(), True
    except NoResultFound:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.flush()
            return created, False
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one(), True

