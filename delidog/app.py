import falcon
from falcon.routing import CompiledRouter
from delidog.resources import send
from delidog.db import PeeweeConnectionMiddleware

middleware = [
    PeeweeConnectionMiddleware(),
]

router = CompiledRouter()
router.add_route('send/', send.Resource())

api = falcon.API(
    router=router,
    middleware=middleware
)
