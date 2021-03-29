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

        chats = Chat.get_chats_by_token(token)
        for chat in chats:
            send_message(
                chat,
                text,
                disable_notification
            )

        resp.status = falcon.HTTP_200

    @jsonschema.validate(json_schema)
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        for message in req.media:
            chats = Chat.get_chats_by_token(message.get('token'))
            for chat in chats:
                send_message(
                    chat,
                    message.get('text'),
                    message.get('disable_notification')
                )
        resp.status = falcon.HTTP_200
