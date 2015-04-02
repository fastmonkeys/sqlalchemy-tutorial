import sqlalchemy as sa

from db import Base


class Country(Base):
    __tablename__ = 'country'

    code = sa.Column(sa.String(3), primary_key=True)
    code2 = sa.Column(sa.String(2), nullable=False)
    name = sa.Column(sa.Unicode, nullable=False)
    continent = sa.Column(sa.Unicode, nullable=False)
    region = sa.Column(sa.Unicode, nullable=False)
    surface_area = sa.Column(sa.Float, nullable=False)
    independence_year = sa.Column(sa.SmallInteger)
    population = sa.Column(sa.Integer, nullable=False)
    life_expectancy = sa.Column(sa.Float, nullable=False)
    gnp = sa.Column(sa.Numeric(10, 2))
    gnp_old = sa.Column(sa.Numeric(10, 2))
    local_name = sa.Column(sa.Unicode, nullable=False)
    government_form = sa.Column(sa.Unicode, nullable=False)
    head_of_state = sa.Column(sa.Unicode)
    capital_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('city.id'),
        nullable=False
    )
    capital = sa.orm.relationship('City', foreign_keys=[capital_id])

    def __repr__(self):
        return "<Country(name='{0}')>".format(self.name)


class City(Base):
    __tablename__ = 'city'

    id = sa.Column(sa.Integer, primary_key=True)
    country_code = sa.Column(
        sa.String(3),
        sa.ForeignKey('country.code'),
        nullable=False
    )
    country = sa.orm.relationship('Country', foreign_keys=[country_code])
    name = sa.Column(sa.Unicode, nullable=False)
    district = sa.Column(sa.Unicode, nullable=False)
    population = sa.Column(sa.Integer, nullable=False)

    def __repr__(self):
        return "<City(name='{0}')>".format(self.name)


class Language(Base):
    __tablename__ = 'language'

    country_code = sa.Column(
        sa.String(3),
        sa.ForeignKey('country.code'),
        nullable=False,
        primary_key=True
    )
    country = sa.orm.relationship('Country', backref='language')
    language = sa.Column(sa.Unicode, nullable=False, primary_key=True)
    is_official = sa.Column(sa.Boolean, nullable=False)
    percentage = sa.Column(sa.Float, nullable=False)

    def __repr__(self):
        return "<Language(name='{0}', country_code='{1}')>".format(
            self.language,
            self.country_code
        )
