class OTPException(Exception):
  pass

class LimitedException(OTPException):
  pass

class InvalidOTPException(OTPException):
  pass
