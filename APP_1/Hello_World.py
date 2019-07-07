import APP_1.logerror as lg

try:
    a = 10
    b = 'a'
    c = a/b
except Exception as e:
    lg.log_exception(e)
