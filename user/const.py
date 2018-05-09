from core.const import Const

class USER_STATUS(Const):
  CREATED = 1
  INACTIVE = 3
  ACTIVE = 5

  choices = [
    (CREATED, 'Created'),
    (INACTIVE, 'Inactive'),
    (ACTIVE, 'Active'),
  ]

