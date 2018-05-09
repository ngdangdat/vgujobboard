from core.const import Const

class GENDER(Const):
  MALE = 1
  FEMALE = 3
  UNDEFINED = 5

GENDER_CHOICES = [
  (GENDER.MALE, 'Male'),
  (GENDER.FEMALE, 'Female'),
  (GENDER.UNDEFINED, 'Undefined'),
]

class MAJOR(Const):
  UNDEFINED = 1
  EEIT = 3
  FA = 5

  choices = [
    (EEIT, 'EEIT'),
    (FA, 'FA'),
  ]


MIN_INTAKE = 2008

class USER_STATUS(Const):
  CREATED = 1
  INACTIVE = 3
  ACTIVE = 5

  choices = [
    (CREATED, 'Created'),
    (INACTIVE, 'Inactive'),
    (ACTIVE, 'Active'),
  ]

class OTP_INTERVAL(Const):
  OTP_LIVE_TIME = 60 * 3
  OTP_REQUEST = 60 * 5
  OTP_CHECK = 60 * 5

class OTP_LIMIT(Const):
  OTP_REQUEST = 3
  OTP_CHECK = 5
