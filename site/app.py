from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import JSONResponse, TemplateResponse

app = Starlette(template_directory='templates')
app.mount('/static', StaticFiles(directory='statics'), name='static')
app.template_env.trim_blocks = True
app.template_env.lstrip_blocks = True

@app.route('/')
async def index(request):
  template = app.get_template('index.html')
  context = dict(request=request, title='Index')
  return TemplateResponse(template, context)
