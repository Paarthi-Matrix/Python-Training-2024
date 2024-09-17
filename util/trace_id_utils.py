import logging
import uuid
import threading

thread_local = threading.local()


def set_trace_id(trace_id):
    thread_local.trace_id = trace_id


def get_trace_id():
    return getattr(thread_local, 'trace_id', 'N/A')


class TraceIDFormatter(logging.Formatter):
    """
    This class used to formate the logger info by considering the Trace ID
    """
    def format(self, record):
        record.trace_id = get_trace_id()
        return super().format(record)


def generate_trace_id():
    return str(uuid.uuid4())
