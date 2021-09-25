# Create your views here.
import numpy as np
from django.shortcuts import render
# import django_tables2 as table
# from django.template.context_processors import request
# from django.forms import formset_factory
# from .tables import linprog_table
from .forms import InventoryForm, QueuingForm, linprogForm
# sys.path.append('..')
from .coding.inventory_models import solving_model
from .coding.queuing_models import Models
# from django.views.generic import ListView
# from .models import linprog_vars


def linprog(browser):
    """
    Load linprog page
    :param browser: the method to respond to browser's calling
    :return:
    """
    context = {'formset': linprogForm}
    return render(browser, 'linprog/linprog.html', context)


def torp(browser):
    context = {}
    return render(browser, 'home/index.html', context)


def inventory(browser):
    context = {'form': InventoryForm}
    return render(browser, 'inventory/inventory.html', context)


def get_linprog_results(browser):
    if browser.method == 'POST':
        form = linprogForm(browser.POST)
        if form.is_valid():
            data = form.cleaned_data.get('problem').replace('\n', '').replace('*', '')
            extract_linprog_data(data)
            for item in data.split('\r'):
                if '\t' in item:
                    print(item.split('\t'))
                else:
                    if len(item) > 0:
                        print(item)

            print('data:',  data.split('\n'), 'type:', type(data))
        context = {}
        return render(browser, 'linprog/linprog_res.html', context)


def extract_linprog_data(data):
    """
    Parse the data extracted from textarea
    :param data: (str) string data
    :return: the data parsed ready to solve
    """

    for item in data.replace('\n', '').split('\r'):
        # cj = None
        if 'max' in item.lower() or 'min' in item.lower():
            cj = extract_cj(item)
            print('cj:', cj)



def extract_cj(item):
    """
    Extract objective function data
    return: dictionary of Cj and value
    """
    cj = {'error': ''}
    if 'max' in item.lower() or 'min' in item.lower():
        if 'max' in item.lower():
            print('max problem')
        else:
            print('min problem')

        obj_text = item.split('=')[1]
        variables = obj_text.split('+')
        all_vars = []
        for item in variables:
            print('item:', item)
            if '-' in item:
                all_vars.extend(item.split('-'))
            else:
                all_vars.append(item)
        print(all_vars)
        for item in all_vars:

            print('my item:', item)
            var = separate_var_coef(item)
            print('my var:', var)
            if var['error'] == '':
                cj['{}'.format(var['subindex'])] = var['coefficient']
            else:
                cj['error'] = var['error']
                break

            # cj[item.split('x')[1]] = 1
            # try:
            #     if item.split('x')[0] == '':
            #         cj[item.split('x')[1]] = 1
            #     else:
            #         cj[item.split('x')[1]] = float(item.split('x')[0])
            # except ValueError:
            #     cj['error'] = 'Please check Cj of X{}'.format(item.split('x')[1])
            #     break
    return cj


def separate_var_coef(item):
    """
    Divide var into elements
    return: dictionary ('coefficient': 'value', 'subindex': 'value, 'error': '')
    """
    var_ready = {'error': ''}
    split_var = item.split('x')
    print('split:', split_var)
    try:
        if split_var[0] == '':
            # var_ready[item.split('x')[1]] = 1
            var_ready['coefficient'] = 1
            var_ready['subindex'] = split_var[1]
        else:
            # var_ready[item.split('x')[1]] = float(item.split('x')[0])
            var_ready['subindex'] = split_var[1]
            var_ready['coefficient'] = float(split_var[0])
    except ValueError:
        var_ready['error'] = 'Please check Cj of X{}'.format(split_var[1])
        return var_ready
    return var_ready


def get_inv_results(browser):
    if browser.method == 'POST':
        form = InventoryForm(browser.POST)
        if form.is_valid():
            unit = form.cleaned_data.get('unit')
            time_unit = form.cleaned_data.get('time_unit')
            model = form.cleaned_data.get('model')
            demand = form.cleaned_data.get('demand')
            unit_cost = form.cleaned_data.get('unit_cost')
            order_cost = form.cleaned_data.get('order_cost')
            unit_holding_cost = form.cleaned_data.get('unit_holding_cost')
            unit_shortage_cost = form.cleaned_data.get('unit_shortage_cost')
            production_rate = form.cleaned_data.get('production_rate')
            # FIX context on queuing
            data = {
                'unit': unit,
                'time_unit': time_unit,
                'model': model,
                'demand': demand,
                'unit_cost': unit_cost,
                'order_cost': order_cost,
                'unit_holding_cost': unit_holding_cost,
                'unit_shortage_cost': unit_shortage_cost,
                'production_rate': production_rate}
            a = data.get('demand')
            c = data.get('unit_cost')
            k = data.get('order_cost')
            h = data.get('unit_holding_cost')
            u = data.get('unit_shortage_cost')
            r = data.get('production_rate')
            model_req = {'General': (a, c, k, h, u, r),
                         'EPQ': (a, c, k, h, r),
                         'EOQ': (a, k, h),
                         'EOQ+': (a, k, h, u)}
            data = (model, unit, time_unit, a, c, k, h, u, r)
            good = check_model_requirements(model, model_req)
            print(good)
            if good:
                context = solving_model(data)
                print('context:', context)
                # return render(request, 'queuing/inventory_res.html', {'queuing': context})
                return render(browser, 'inventory/inventory_res.html', context)
            else:
                # request.method = 'POST'
                context = {}
                return render(browser, 'inventory/inventory.html', context)
        else:
            # return HttpResponse("Please, use the website browsing to get this page.")
            context = {}
            return render(browser, 'inventory/inventory.html', context)


def queuing(browser):
    context = {'form': QueuingForm}
    return render(browser, 'queuing/queuing.html', context)


def get_queue_results(browser):
    if browser.method == 'POST':
        form = QueuingForm(browser.POST)
        if form.is_valid():
            # unit = form.cleaned_data.get('unit')
            # time_unit = form.cleaned_data.get('time_unit')
            servers = form.cleaned_data.get('servers')
            pop_queue = form.cleaned_data.get('pop_queue').upper()
            arrival = form.cleaned_data.get('arrival')
            service = form.cleaned_data.get('service')
            n_clients = form.cleaned_data.get('n_clients')
            waiting_cost = form.cleaned_data.get('waiting_cost')
            service_cost = form.cleaned_data.get('service_cost')
            clients_lost_cost = form.cleaned_data.get('clients_lost_cost')
            try:
                if 'LQ' in pop_queue:
                    lq_type = 'cf'
                    # ls_type = 'inf'
                    limited_queue = float(pop_queue[3:])
                    limited_source = np.inf
                elif 'LS' in pop_queue:
                    lq_type = 'fl'
                    # ls_type = 'fl'
                    limited_queue = np.inf
                    limited_source = float(pop_queue[3:])
                else:
                    lq_type = "∞"
                    limited_queue = np.inf
                    limited_source = np.inf
                print('serv;', servers, 'pop_que:', pop_queue, 'lS:', limited_source, 'LQ:', limited_queue)
                model = 'M/M/{}:{},FIFO'.format([1 if servers == 1 else 'S'][0], lq_type.upper())
                solution = Models(arrival, service, limited_queue, limited_source, n_clients, servers, service_cost,
                                  waiting_cost,
                                  clients_lost_cost).solution
                print('solution:', solution)
                context = {
                    'model': [model.replace('CF', 'LQ') if 'CF,' in model else
                              model.replace('FL', 'LS') if 'FL' in model else model.replace('INF', 'INF')][0],
                    'lambda': arrival,
                    'mu': service,
                    'rho': solution.get('rho'),
                    'L': solution.get('L'),
                    'Lq': solution.get('Lq'),
                    'W': solution.get('W'),
                    'Wq': solution.get('Wq'),
                    'Po': solution.get('Po'),
                    'Pn': solution.get('Pn'),
                    'Pto': solution.get('Pto'),
                    'P1': solution.get('P1'),
                    'Pmclient': solution.get('Pmclient'),
                    'Pm': solution.get('Pm'),
                    'Ct': solution.get('Ct'),
                }
                return render(browser, 'queuing/queuing_res.html', context)
            except ValueError:
                context = {
                    'model': "Check the field 'Size of population/queue'",
                    'lambda': "Check the field 'Size of population/queue'",
                    'mu': "Check the field 'Size of population/queue'",
                    'rho': "Check the field 'Size of population/queue'",
                    'L': "Check the field 'Size of population/queue'",
                    'Lq': "Check the field 'Size of population/queue'",
                    'W': "Check the field 'Size of population/queue'",
                    'Wq': "Check the field 'Size of population/queue'",
                    'Po': "Check the field 'Size of population/queue'",
                    'Pn': "Check the field 'Size of population/queue'",
                    'Pto': "Check the field 'Size of population/queue'",
                    'P1': "Check the field 'Size of population/queue'",
                    'Pmclient': "Check the field 'Size of population/queue'",
                    'Pm': "Check the field 'Size of population/queue'",
                    'Ct': "Check the field 'Size of population/queue'",
                }
                return render(browser, 'queuing/linprog_res.html', context)
    else:
        # return HttpResponse("Please, use the website browsing to get this page.")
        context = {}
        return render(browser, 'queuing/linprog_res.html', context)


def check_model_requirements(model, model_req):
    if model == 'General':
        requirements = inside_model_req(model_req.get('General'))
    elif '(EOQ)' in model:
        requirements = inside_model_req(model_req.get('EOQ'))
    elif 'short' in model:
        requirements = inside_model_req(model_req.get('EOQ+'))
    else:
        requirements = inside_model_req(model_req.get('EPQ'))
    return requirements


def inside_model_req(req):
    data_is_ok = True
    for item in req:
        if not item > 0:
            data_is_ok = False
            break
    return data_is_ok
