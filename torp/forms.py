from cProfile import label

from django import forms


class InventoryForm(forms.Form):
    unit = forms.CharField(label='Unit (products, cars, etc.):', max_length=10, help_text='', min_length=0,
                           empty_value='products', label_suffix="-")
    time_unit = forms.CharField(label="Time's unit (month, day, etc.):", max_length=10, help_text='', empty_value='day')
    my_options = (('General', 'General'), ('Economic Production Quantity (EPQ)', 'Economic Production Quantity (EPQ)'),
                  ('Economic Order Quantity (EOQ)', 'Economic Order Quantity (EOQ)'),
                  ('EOQ with shortage', 'EOQ with shortage'))
    model = forms.ChoiceField(choices=my_options, label='Model:')
    demand = forms.FloatField(label='Demand (a):', min_value=0, help_text='')
    unit_cost = forms.FloatField(label='Unit cost (c):', help_text=' :')
    order_cost = forms.FloatField(label='Order cost (k):', min_value=0, help_text=' ')
    unit_holding_cost = forms.FloatField(label='Unit holding cost (h):', min_value=0, help_text=' ')
    unit_shortage_cost = forms.FloatField(label='Unit shortage cost (u):', help_text=' ')
    production_rate = forms.FloatField(label='Production rate (r):', help_text='')


class QueuingForm(forms.Form):
    # unit = forms.CharField(label='Unit (products, cars, etc.):', max_length=10, help_text='', min_length=0,
    #                        empty_value='products')
    # time_unit = forms.CharField(label="Time's unit (month, day, etc.):", max_length=10, help_text='', empty_value='day')
    servers = forms.IntegerField(label="Time's unit (month, day, etc.):")
    pop_queue = forms.CharField(label='Size of Population/Queue (INF, LQ=#, LS=#:)', max_length=7)
    arrival = forms.FloatField()
    service = forms.FloatField()
    n_clients = forms.FloatField()
    waiting_cost = forms.FloatField()
    service_cost = forms.FloatField()
    clients_lost_cost = forms.FloatField()


class Inventory_resultsForm(forms.Form):
    model = forms.CharField(label='Model:', max_length=30, help_text='')
    Q = forms.FloatField(label='Order quantity(Q):', min_value=0.00000001, help_text='')
    S = forms.FloatField(label='Maximum inventory(S):', min_value=0.00000001, help_text='')
    t1 = forms.FloatField(label='Interval of time 1 (t1):', min_value=0.00000001, help_text='')
    t2 = forms.FloatField(label='Interval of time 1 (t2):', min_value=0.00000001, help_text='')
    t3 = forms.FloatField(label='Interval of time 1 (t3):', min_value=0.00000001, help_text='')
    t4 = forms.FloatField(label='Interval of time 1 (t4):', min_value=0.00000001, help_text='')
    B = forms.FloatField(label='Deficit (B):', min_value=0.00000001, help_text='')
    T = forms.FloatField(label='Period(T):', min_value=0.00000001, help_text='')
    f = forms.FloatField(label='Frequency(f):', min_value=0.00000001, help_text='')
    PC = forms.FloatField(label='Production cost:', min_value=0.00000001, help_text='')
    DC = forms.FloatField(label='Deficit cost:', min_value=0.00000001, help_text='')
    IC = forms.FloatField(label='Inventory cost:', min_value=0.00000001, help_text='')
    TC = forms.FloatField(label='Total cost:', min_value=0.00000001, help_text='')


class linprogForm(forms.Form):
    problem = forms.CharField(label='x1', label_suffix='', widget=forms.Textarea(attrs={'style': 'width: 450px'}),
                              initial='vars:\r\robjective:\r\rconstraints:')
    # x2 = forms.FloatField(label='x2', label_suffix='', widget=forms.TextInput(attrs={'style': 'width: 45px'}))
    # x3 = forms.FloatField(label='x3', label_suffix='', widget=forms.TextInput(attrs={'style': 'width: 45px'}))
    # x4 = forms.FloatField(label='x4', label_suffix='', widget=forms.TextInput(attrs={'style': 'width: 45px'}))
    # x5 = forms.FloatField(label='x5', label_suffix='', widget=forms.TextInput(attrs={'style': 'width: 45px'}))
    # direction = forms.CharField(label='direction', label_suffix='', max_length=2, widget=forms.TextInput(attrs={'style': 'width: 15px'}))
    # right_hs = forms.FloatField(label='right_hs', label_suffix='', widget=forms.TextInput(attrs={'style': 'width: 45px'}))
