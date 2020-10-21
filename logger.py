from datetime import datetime

def get_log_to (function):
    def create_recording(*args, **kwargs):
        result = function(*args, **kwargs)
        with open('file.txt', 'a') as f:
            f.write(f'Running {function.__name__}: {datetime.now()}'+ '\n')
            f.write(f'      Parameters: {args}, {kwargs}'+ '\n')
            f.write(f'      Result: {result}'+ '\n')
        return result
    return create_recording


def get_log_to_file(filename):
    def get_log_to (function):
        def create_recording(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(f'Running {function.__name__}: {datetime.now()}'+ '\n')
                f.write(f'      Parameters: {args}, {kwargs}'+ '\n')
                f.write(f'      Result: {result}'+ '\n')
            return result
        return create_recording
    return get_log_to
