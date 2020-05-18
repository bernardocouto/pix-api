from bottle import response
from configurations.log import get_logger
from factory import create_application

import services.health_check
import services.pix

application = create_application()

application.merge(services.health_check.application)
application.merge(services.pix.application)

logger = get_logger('main')


@application.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Accept, Accept-Type, Authorization, Content-Type, Origin, ' \
                                                       'X-CSRF-Token, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, OPTIONS, POST, PUT'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@application.route('/<:re:.*>', method='OPTIONS')
def enable_cors_generic_route():
    enable_cors()


def main():
    application.run(debug=True, host='0.0.0.0', port=8080, reloader=True)


if __name__ == '__main__':
    main()
