# -*- coding: utf-8 -*-
import numpy as np
from numpy import array, where, inf
from math import pow as power, fsum

from math import factorial


class Models:
    def __init__(self, my_lambda, mu, queue_population=inf, source_population=inf, n=0, servers=1, cs=0, cw=0, cp=0):
        # if str(source_population).lower() == 'inf':
        #     source_pop = 1000000
        # else:
        #     source_pop = source_population
        data = array([my_lambda, mu, servers, n, cs, cw, queue_population, source_population])
        print(data)
        data = where(data < 0, abs(data), data)
        self.__lambda = data[0]
        self.__mu = data[1]
        s = int(data[2])
        n = int(data[3])
        cs = data[4]
        cw = data[5]
        if 0 < queue_population != inf:
            m = int(data[6] + s)
            source = 'cf'
        elif 0 < source_population != inf:
            m = int(data[7])
            source = 'fl'
        else:
            source = 'inf'
            m = 0
        self.__rho = self.__lambda / (self.__mu * s)  # Overall utilization
        self.__p_n = 0  # Probability of n unit in the system
        self.__L = 0  # Average number of customer in the system
        self.__Lq = 0  # Average number of customer in the queue
        self.__W = 0  # Average time customer spends in the system
        self.__Wq = 0  # Average time customer spends in the queue
        self.__po = 0  # Probability that system is idle
        self.__p1 = 0  # Probability that system is busy
        self.__pto = 0  # Probability of customer enter to system and don't have to wait to being served
        self.__pm = 0  # Fraction of customers that can't enter to the system and then leave it
        self.__Cw = 0  # Service cost
        self.__Cs = 0  # Waiting cost
        self.__Ct = 0  # Total cost
        self.__pm_client = 0  # Average number of customer being balked
        self.__model = ''
        self.solution = {}
        self.__select_model(n, source, s, cw, cs, cp, m)
        self.__form_solution()

    def __select_model(self, n, source, s, cw, cs, cp, m):
        if s == 1 and source == 'inf':
            # print('Running Model: M/M/1:Inf,FIFO')
            self.__model = 'M/M/1:Inf,FIFO'
            self.__mm1inf(n, s, cw, cs)
        elif s > 1 and source == 'inf':
            # print('Running Model M/M/S:Inf,FIFO')
            self.__model = 'M/M/S:Inf,FIFO'
            self.__mmsinf(n, s, cw, cs)
        elif s == 1 and source == 'cf':
            # print('Running Model M/M/1:CF,FIFO')
            self.__model = 'M/M/1:CF,FIFO'
            self.__mm1cf(n, s, cw, cs, cp, m)
        elif s > 1 and source == 'cf':
            # print('Running Model M/M/S:CF,FIFO')
            self.__model = 'M/M/S:CF,FIFO'
            self.__mmscf(n, s, cw, cs, m)
        elif s == 1 and source == 'fl':
            # print('Running Model M/M/1:FL,FIFO')
            self.__model = 'M/M/1:FL,FIFO'
            self.__mm1fl(n, s, cw, cs, m)
        elif s > 1 and source == 'fl':
            # print('Running Model M/M/S:FL,FIFO')
            self.__model = 'M/M/S:FL,FIFO'
            self.__mmsfl(n, s, m)

    def __form_solution(self):
        self.__pm_client = self.__pm * self.__lambda
        self.solution = {
            'model': self.__model,
            'lambda': self.__lambda,
            'mu': self.__mu,
            'rho': float(self.__rho).__round__(7),
            'L': float(self.__L).__round__(7),
            'Lq': float(self.__Lq).__round__(7),
            'W': float(self.__W).__round__(7),
            'Wq': float(self.__Wq).__round__(7),
            'Po': float(self.__po).__round__(7),
            'Pn': float(self.__p_n).__round__(7),
            'Pto': float(self.__pto).__round__(7),
            'P1': float(self.__p1).__round__(7),
            'Pmclient': float(self.__pm_client).__round__(7),
            'Pm': float(self.__pm).__round__(7),
            'Cs': float(self.__Cs).__round__(7),
            'Cw': float(self.__Cw).__round__(7),
            'Ct': float(self.__Ct).__round__(7)
        }

    def __mm1inf(self, n, s, cw, cs):
        self.__p_n = power(self.__rho, n) - power(self.__rho, n + 1)
        self.__L = self.__rho / (1 - self.__rho)
        self.__Lq = power(self.__lambda, 2) / (self.__mu * (self.__mu - self.__lambda))
        self.__W = 1 / (self.__mu - self.__lambda)
        self.__Wq = self.__lambda / (self.__mu * (self.__mu - self.__lambda))
        self.__po = self.__p_n_mm1inf(0)
        self.__pto = self.__po
        self.__p1 = 1 - self.__po
        self.__Cw = cw * self.__L
        self.__Cs = cs * s
        self.__Ct = self.__Cw + self.__Cs

    def __p_n_mm1inf(self, n):
        p_n = power(self.__rho, n) * (1 - self.__rho)
        return p_n

    def __mmsinf(self, n, s, cw, cs):
        self.__po = 1 / (
                sum(power(self.__lambda / (self.__mu * factorial(n)), i) for i in range(s)) + power(self.__lambda
                                                                                                    / self.__mu,
                                                                                                    s) / (
                        factorial(s) * (1 - self.__rho)))
        self.__p_n = self.__p_n_mmsinf(n, s)
        self.__Lq = self.__po * power(self.__lambda / self.__mu, s) * self.__rho / (factorial(s) * power(1 - self.__rho,
                                                                                                         2))
        self.__L = self.__Lq + self.__lambda / self.__mu
        self.__W = self.__L / self.__lambda
        self.__Wq = self.__Lq / self.__lambda
        self.__p1 = power(self.__lambda / self.__mu, s) * self.__po / (factorial(s) * (1 - self.__rho))
        self.__pto = 1 - self.__p1
        self.__Cw = cw * self.__L
        self.__Cs = cs * s
        self.__Ct = self.__Cw + self.__Cs

    def __p_n_mmsinf(self, n, s):
        if 0 <= n <= s:
            p_n = (power(self.__lambda / self.__mu, n) * self.__po) / factorial(n)
        else:
            p_n = (power(self.__lambda / self.__mu, n) * self.__po) / factorial(s) * power(s, n - s)
        return p_n

    def __mm1cf(self, n, s, cw, cs, cp, m):
        if self.__rho != 1:
            self.__po = (1 - self.__rho) / (1 - power(self.__rho, m + 1))
            self.__L = (self.__rho / (1 - self.__rho)) - ((m + 1) * power(self.__rho, m + 1) / (1 - power(self.__rho,
                                                                                                          m + 1)))
            self.__Lq = self.__L - (1 - self.__po)
            my_lambda_bar = self.__mu * (1 - self.__po)
            self.__W = self.__L / my_lambda_bar
            self.__Wq = self.__Lq / my_lambda_bar
        else:
            self.__L = m / 2
            self.__Lq = (sum(i - 1 for i in range(1, m + 1)) / (m + 1))
            my_lambda_bar = self.__lambda * (m / (m + 1))
            self.__W = self.__L / my_lambda_bar
            self.__Wq = self.__Lq / my_lambda_bar
            self.__po = self.__p_n_mm1cf(0, m)
        self.__p_n = self.__p_n_mm1cf(n, m)
        self.__pm = self.__p_n_mm1cf(m, m) * self.__lambda
        self.__pm_client = self.__p_n_mm1cf(m, m)
        self.__pto = 1 - self.__po
        self.__p1 = 1 - self.__pto
        # ---------- COSTS ------------
        self.__Cw = cw * self.__L
        self.__Cs = cs * s
        self.__Ct = self.__Cw + self.__Cs + cp * self.__pm * self.__lambda

    def __p_n_mm1cf(self, n, m):
        if self.__rho != 1:
            p_n = power(self.__rho, n) * self.__po
        else:
            p_n = 1 / (m + 1)
        return p_n

    def __mmscf(self, n, s, cw, cs, m):
        self.__po = self.__p_n_mmscf(0, s, m)
        self.__p_n = self.__p_n_mmscf(n, s, m)
        self.__Lq = self.__po * power(self.__lambda / self.__mu, s) * self.__rho * (1 - power(self.__rho, m - s) -
                                                                                    (m - s) * power(self.__rho, m - s) *
                                                                                    (1 - self.__rho)) / (factorial(s) *
                                                                                                         power(
                                                                                                             1 -
                                                                                                             self.__rho,
                                                                                                             2))
        self.__L = fsum(i * self.__p_n_mmscf(i, s, m) for i in range(s)) + self.__Lq + s * (
                1 - sum(self.__p_n_mmscf(i, s, m)
                        for i in range(s)))
        if n == m:
            self.__pm = self.__p_n
        else:
            self.__pm = self.__p_n_mmscf(m, s, m) * (m - s)

        my_lambda_bar = self.__lambda * (1 - self.__pm)
        self.__W = self.__L / my_lambda_bar
        self.__Wq = self.__Lq / my_lambda_bar
        self.__pto = fsum(self.__p_n_mmscf(i, s, m) for i in range(s))
        # ------------ COSTS ----------------
        self.__p1 = 1 - self.__pto
        self.__Cw = cw * self.__L
        self.__Cs = cs * s
        self.__Ct = self.__Cw + self.__Cs

    def __p_n_mmscf(self, n, s, m):
        if n == 0:
            mi_p_n = 1 / (1 + fsum(power(self.__lambda / self.__mu, i) / factorial(i) for i in range(1, s + 1)) +
                          (power(self.__lambda / self.__mu, s) / factorial(s)) *
                          fsum(power(self.__lambda / (s * self.__mu), i - s) for i in range(s + 1, m + 1)))
        elif 0 < n <= s - 1:
            mi_p_n = power(self.__lambda / self.__mu, n) * self.__po / factorial(n)
        elif s <= n <= m:
            mi_p_n = power(self.__lambda / self.__mu, n) * self.__po / (factorial(s) * power(s, n - s))
        else:
            mi_p_n = 0
        return mi_p_n

    def __mm1fl(self, n, s, cw, cs, m):
        self.__po = 1 / (
            fsum(factorial(m) / factorial(m - i) * power(self.__lambda / self.__mu, i) for i in range(m + 1)))
        self.__p_n = self.__p_n_mm1fl(n, m)
        self.__L = m - (self.__mu / self.__lambda) * (1 - self.__po)
        self.__Lq = self.__L - (1 - self.__po)
        my_lambda_var = self.__lambda * (m - self.__L)
        self.__W = self.__L / my_lambda_var
        self.__Wq = self.__Lq / my_lambda_var
        self.__pto = 1 - self.__po
        self.__p1 = 1 - self.__pto
        self.__Cw = cw * self.__L
        self.__Cs = cs * s
        self.__Ct = (self.__Cw + self.__Cs) / m

    def __p_n_mm1fl(self, n, m):
        p_n = (factorial(m) / factorial(m - n)) * power(self.__lambda / self.__mu, n) * self.__po
        return p_n

    def __mmsfl(self, n, s, m):
        self.__po = 1 / (
                fsum(factorial(m) / (factorial(m - i) * factorial(i)) * power(self.__lambda / self.__mu, i) for i
                     in range(s)) +
                fsum(factorial(m) / (factorial(m - i) * factorial(s) * power(s, i - s)) * power(self.__lambda /
                                                                                                self.__mu, i) for i
                     in range(s, m + 1)))
        self.__p_n = self.__p_n_mmsfl(n, s, m)
        self.__Lq = fsum((i - s) * self.__p_n_mmsfl(i, s, m) for i in range(s, m + 1))
        self.__L = fsum(i * self.__p_n_mmsfl(i, s, m) for i in range(s)) + self.__Lq + s * (
                1 - fsum(self.__p_n_mmsfl(i, s, m)
                         for i in range(s)))
        my_lambda_var = self.__lambda * (m - self.__L)
        self.__W = self.__L / my_lambda_var
        self.__Wq = self.__Lq / my_lambda_var
        self.__pto = fsum(self.__p_n_mmsfl(i, s, m) for i in range(s))
        self.__p1 = 1 - self.__pto

    def __p_n_mmsfl(self, n, s, m):
        if 0 <= n < s:
            p_n = factorial(m) / (factorial(m - n) * factorial(n)) * power(self.__lambda / self.__mu, n) * self.__po
        elif s <= n <= m:
            p_n = factorial(m) / (factorial(m - n) * factorial(s) * power(s, n - s)) * power(self.__lambda / self.__mu,
                                                                                             n) * self.__po
        else:
            p_n = 0
        return p_n

# my_lambda = 6
# miu = 8
# n = 0
# servers = 1
# queue_population = 6
# source_population = inf

# model = Models(my_lambda, miu, queue_population, source_population, n, servers, cs=5, cw=5, cp=2)  # my_lambda, mu,
# source='inf', s=1, n=0, cs=0, cw=0 print('Customer arrival rate(per hour) Lambda = ', my_lambda) print('Service
# rate(per server per hour) Miu = ', miu) print('Overall system utilization (rho) = ', model.rho) print('Average
# number of customer in the system (L) = ', model.L) print('Average number of customer in the queue (Lq) = ',
# model.Lq) print('Average time customers spend in the system (W) = ', model.W) print('Average time customers spends
# in the queue (Wq) = ', model.Wq) print('The probability that the system is idle (Po) = ', model.po) print(
# 'Probability of {0} unit(s) in the system p({0}) = '.format(n), model.p_n) print("The probability an arriving
# customer and don't have to wait p(T=0) = ", model.pto) print('The probability an arriving customer and have to wait
# p(T>0) = ', model.p1) print('Average number of customer being balked (Pm) = ', model.pm) print('The probability an
# arriving customer and and leave the system (Pm) = ', model.pm_client) print('Cw=', model.Cw) print('Cs=',
# model.Cs) print('Ct=', model.Ct)
