sessions = {}


class ContentSessionService:


    def create(
            self,
            user_id,
            content_type
    ):

        sessions[user_id] = {
            "content_type": content_type,
            "status": "WAITING_INPUT"
        }



    def get(
            self,
            user_id
    ):

        return sessions.get(user_id)



    def remove(
            self,
            user_id
    ):

        if user_id in sessions:
            del sessions[user_id]