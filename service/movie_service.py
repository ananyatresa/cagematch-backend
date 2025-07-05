from model.movie_req_res import MovieResponse


class MovieService:
    def __init__(self, config):
        self.get_config = config

    def get_movie(self, req):
        mood = req.mood
        nick_cage_config = self.get_config['nick_cage']
        if mood.lower() not in nick_cage_config['moods']:
            return "Mood unmatched!! Pick a valid mood for Nick Cage"

        movies = [{'name': movie, 'image': details['image']} for movie, details in nick_cage_config['movies'].items()
                  if mood.lower() in details['mood']]

        return {"result": MovieResponse(mood=mood, movies=movies)}
