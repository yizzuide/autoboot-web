
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette_csrf import CSRFMiddleware


class UniformCSRFMiddleware(CSRFMiddleware):
  
  def _get_error_response(self, request: Request) -> Response:
    return JSONResponse(content={'code': 400, 'message': 'CSRF Failed'}, status_code=200)
