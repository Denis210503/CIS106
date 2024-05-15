def compute_next_month_sales(month, sales):
    forecast_percent = 0

    if month in ['Jan', 'Feb', 'Mar']:
        forecast_percent = 0.10
    elif month in ['Apr', 'May', 'Jun']:
        forecast_percent = 0.15
    elif month in ['Jul', 'Aug', 'Sep']:
        forecast_percent = 0.20
    elif month in ['Oct', 'Nov', 'Dec']:
        forecast_percent = 0.25

    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales
