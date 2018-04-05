

class Body:

    supported_characteristics = ['m', 'mass',
                         'J', 'inertia']

    def __init__(self, options):
        for key in options.keys():
            if key in Body.supported_characteristics:
                val = options[key]
                if key in ['m', 'mass']:
                    self.mass = val
                elif key in ['J', 'inertia']:
                    self.J = val
            else:
                Log.print('Not supported key:{}'.format(key))