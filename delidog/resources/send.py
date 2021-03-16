import falcon
from falcon.media.validators import jsonschema
from delidog.bot import send_message
from delidog.models import Chat

json_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "token": {
                "type": "string",
                "minLength": 1,
                "maxLength": 50
            },
            "text": {
                "type": "string",
                "minLength": 1
            },
            "disable_notification": {
                "type": "boolean",
                "default": False
            }
        }
    }
}


class Resource(object):
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        token = req.params.get('token')
        if token is None:
            raise falcon.HTTP_BAD_REQUEST

        text = req.params.get('text')
        if text is None:
            raise falcon.HTTP_BAD_REQUEST

        disable_notification = req.params.get(
            'disable_notification', False)

        send_message(
            Chat.get_chat_by_token(token),
            text,
            disable_notification
        )

        resp.status = falcon.HTTP_200

    @jsonschema.validate(json_schema)
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        for message in req.media:
            send_message(
                Chat.get_chat_by_token(message.token),
                message.text,
                message.disable_notification
            )
        resp.status = falcon.HTTP_200
