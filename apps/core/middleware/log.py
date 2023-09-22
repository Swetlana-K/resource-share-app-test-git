# von der Python-Standard-Bibliothek
import logging

# Get the logging instance
logger = logging.getLogger("logging_mw")  # __name__


def simple_logging_middleware(get_response):
    def middleware(request):
        # : pre-processing -> HTTPRequest
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]

        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logger.info(msg)

        response = get_response(request)  # next middleware or the view

        # Post-Processing
        status_code = response.status_code
        is_closed = response.closed
        reason_phrase = response.reason_phrase
        post_msg = f'Status code: {status_code} | closed: {is_closed} | reason phrase: {reason_phrase}'
        logger.info(post_msg)

        return response

    return middleware


