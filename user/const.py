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

class USER_STATUS(Const):
  CREATED = 1
  INACTIVE = 3
  ACTIVE = 5

  choices = [
    (CREATED, 'Created'),
    (INACTIVE, 'Inactive'),
    (ACTIVE, 'Active'),
  ]

