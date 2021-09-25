import numpy as np


def solving_model(data):
    model, unit, time_unit, a, c, k, h, u, r = data
    model_req = {'General': (a, c, k, h, u, r),
                 'EPQ': (a, c, k, h, r),
                 'EOQ': (a, k, h),
                 'EOQ+': (a, k, h, u)}
    if 'short' in model:
        """EOQ with shortage"""
        model = 'EOQ+'
        q = np.sqrt((2 * a * k / h) * (h / u + 1))
        t = q / a
        f = 1 / t
        b = np.sqrt(2 * a * h * k / (h * u + np.power(u, 2)))
        t2 = b / a
        t1 = np.sqrt(2 * u * k / (a * u * (h + u)))
        t3 = 0
        t4 = 0
        i = q - b
        ic = h * i * t1 / 2
        dc = u * b * t2 / 2
        pc = k
        tc = ic + dc + pc
    elif '(EPQ)' in model:
        """EPQ"""
        model = 'EPQ'
        q = np.sqrt((2 * a * k / h) * (1 / (1 - a / r)))
        t = q / a
        f = 1 / t
        b = 0
        t2 = np.sqrt(2 * k * (1 - a / r) / (a * h))
        t1 = t2 * a / (r - a)
        t3 = 0
        t4 = 0
        i = a * t2
        ic = h * i * (t1 + t2) / 2
        dc = 0
        pc = c * q + k
        tc = ic + dc + pc
    elif '(EOQ)' in model:
        """EOQ"""
        model = 'EOQ'
        q = np.sqrt((2 * a * k / h))
        t = q / a
        f = 1 / t
        b = 0
        t2 = 0
        t1 = t
        t3 = 0
        t4 = 0
        i = q
        ic = h * i * (t1 + t2) / 2
        dc = 0
        pc = k
        tc = ic + dc + pc
    else:
        """General"""
        model = 'General'
        q = np.sqrt((2 * a * k / h) * (1 / (1 - a / r)) * (h / u + 1))
        t = q / a
        f = 1 / t
        b = np.sqrt(2 * a * h * k * (1 - a / r) / ((h + u) * u))
        t2 = np.sqrt(2 * u * k * (1 - a / r) / (a * h * (h + u)))
        t1 = t2 * a / (r - a)
        t3 = np.sqrt(2 * h * k * (1 - a / r) / (a * u * (h + u)))
        t4 = b / (r - a)
        i = a * t2
        ic = h * i * (t1 + t2) / 2
        dc = u * b * (t3 + t4) / 2
        pc = c * q + k
        tc = ic + dc + pc
    decimal_places = 3
    print('q is:', type(q))
    if type(q) not in (float, int, np.float64):
        results = {
            'model': model,
            'unit': unit,
            'time_unit': time_unit,
            'Q': 'Production rate have to be greater than the demand.',
            'I': 'Production rate have to be greater than the demand.',
            't1': 'Production rate have to be greater than the demand.',
            't2': 'Production rate have to be greater than the demand.',
            't3': 'Production rate have to be greater than the demand.',
            't4': 'Production rate have to be greater than the demand.',
            'B': 'Production rate have to be greater than the demand.',
            'T': 'Production rate have to be greater than the demand.',
            'f': 'Production rate have to be greater than the demand.',
            'PC': 'Production rate have to be greater than the demand.',
            'IC': 'Production rate have to be greater than the demand.',
            'DC': 'Production rate have to be greater than the demand.',
            'TC': 'Production rate have to be greater than the demand.',
        }
    elif True in [item == 0 for item in model_req.get(model)]:
        results ={}
    else:
        results = {
            'model': model,
            'unit': unit,
            'time_unit': time_unit,
            'Q': float(q).__round__(decimal_places),
            'I': float(i).__round__(decimal_places),
            't1': float(t1).__round__(decimal_places),
            't2': float(t2).__round__(decimal_places),
            't3': float(t3).__round__(decimal_places),
            't4': float(t4).__round__(decimal_places),
            'B': float(b).__round__(decimal_places),
            'T': float(t).__round__(decimal_places),
            'f': float(f).__round__(decimal_places),
            'PC': float(pc).__round__(decimal_places),
            'IC': float(ic).__round__(decimal_places),
            'DC': float(dc).__round__(decimal_places),
            'TC': float(tc).__round__(decimal_places)
        }
    return results
