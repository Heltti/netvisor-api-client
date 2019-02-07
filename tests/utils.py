import io
import os


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


def get_responses_dir():
    return os.path.join(get_data_dir(), 'responses')


def get_requests_dir():
    return os.path.join(get_data_dir(), 'requests')


def read_file(filename):
    with io.open(filename, 'r', encoding='utf-8') as f:
        return f.read().encode('utf-8')


def get_response_content(filename):
    filename = os.path.join(get_responses_dir(), filename)
    return read_file(filename)


def get_request_content(filename):
    filename = os.path.join(get_requests_dir(), filename)
    return read_file(filename)


def get_response_text(filename):
    return get_response_content(filename).decode('utf-8')
