from . import login_manager, db
# from .main.database import Base, get_session
from flask_login import UserMixin


class RadiusUser(db.Model, UserMixin):
    __tablename__ = 'radiusUsers'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}

    userId = db.Column('userId', db.String(45), nullable=False, primary_key=True)
    archived = db.Column('archived', db.Integer, nullable=False, default=0)
    password = db.Column('pass',db.String(45), nullable=False)
    firstName = db.Column('firstName', db.String(45))
    lastName = db.Column('lastName', db.String(45))
    acctNum = db.Column('acctNum', db.Integer)
    company = db.Column('company', db.String(45))
    companyAddress = db.Column('companyAddress', db.String(100))
    companyAddress2 = db.Column('companyAddress2', db.String(100))
    city = db.Column('city', db.String(45))
    state = db.Column('state', db.String(45))
    zipcode = db.Column('zipcode', db.String(16))
    phone = db.Column('phone', db.String(45))
    emailAlias = db.Column('emailAlias', db.Text)
    question = db.Column('question', db.String(100))
    answer = db.Column('answer', db.String(100))
    notes = db.Column('notes', db.Text)
    parentId = db.Column('parentId', db.String(45))
    maxConnections = db.Column('maxConnections', db.Integer, nullable=False, default=1)
    activationDate = db.Column('activationDate', db.DateTime)
    csr = db.Column('csr', db.String(45))
    email = db.Column('email', db.Integer, nullable=False, default=0)
    staticIP = db.Column('staticIP', db.String(45))
    netmask = db.Column('netmask', db.String(45))
    assocDomains = db.Column('assocDomains', db.Text)
    archDate = db.Column('archDate', db.DateTime)
    package = db.Column('package', db.String(100))
    modemMAC = db.Column('modemMAC', db.String(100))
    webUsage = db.Column('webUseage', db.Integer, default=0)
    webQuota = db.Column('webQuota', db.Integer, default=0)
    emailAddress = db.Column('emailAddress', db.String(45))
    emailQuota = db.Column('emailQuota', db.Integer, default=0)
    emailVirusFilter = db.Column('emailVirusFilter', db.Integer, nullable=False, default=0)
    emailSpamFilter = db.Column('emailSpamFilter', db.Integer, nullable=False, default=0)
    web = db.Column('web', db.Integer, nullable=False, default=0)
    pppDialup = db.Column('pppDialup', db.Integer, nullable=False, default=0)
    dsl = db.Column('DSL', db.Integer, nullable=False, default=0)
    nnsRoam = db.Column('nnsRoam', db.Integer, nullable=False, default=0)
    nationalRoam = db.Column('nationalRoam', db.Integer, nullable=False, default=0)
    ftth = db.Column('FTTH', db.Integer, nullable=False, default=0)
    contentFilter = db.Column('contentFilter', db.Integer, nullable=False, default=0)
    bullOptOut = db.Column('bullOptOut', db.Integer, nullable=False, default=0)
    radiusStaticIP = db.Column('radiusStaticIP', db.String(100))
    emailforward = db.Column('emailforward', db.String(128), nullable=False)
    satLvl = db.Column('satLvl', db.String(10), default='none')
    childExists = db.Column('childExists', db.Integer, nullable=False, default=0)

    def get_id(self):
        return self.userId

    def verify_password(self, password):
        return password == self.password

    def __repr__(self):
        return '<User %r>' % self.userId


@login_manager.user_loader
def load_user(user_id):
    return RadiusUser.query.get(user_id)


# class Permission:
#     FOLLOW = 0x01
#     COMMENT = 0x02
#     WRITE_ARTICLES = 0x04
#     MODERATE_COMMENTS = 0x08
#     ADMINISTER = 0x80
#
#
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     default = db.Column(db.Boolean, default=False, index=True)
#     permissions = db.Column(db.Integer)
#     users = db.relationship('User', backref='role', lazy='dynamic')
#
#     @staticmethod
#     def insert_roles():
#         roles = {
#             'User': (Permission.FOLLOW |
#                      Permission.COMMENT |
#                      Permission.WRITE_ARTICLES, True),
#             'Moderator': (Permission.FOLLOW |
#                           Permission.COMMENT |
#                           Permission.WRITE_ARTICLES |
#                           Permission.MODERATE_COMMENTS, False),
#             'Administrator': (0xff, False)
#         }
#         for r in roles:
#             role = Role.query.filter_by(name=r).first()
#             if role is None:
#                 role = Role(name=r)
#             role.permissions = roles[r][0]
#             role.default = roles[r][1]
#             db.session.add(role)
#         db.session.commit()
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
