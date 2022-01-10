from django.test import TestCase, Client

from film.models import Actor, Movie


class TestMovieViewSet(TestCase):

    def setUp(self) -> None:
        self.actor = Actor.objects.create(name='Test Actor', birthdate='2021-08-01',
                                          picture='https://example.com/artist_3.jpg')
        self.movie = Movie.objects.create(title='Test Movie', actor=self.actor, genre='horror',
                                          movie_url='http://example.com/kunlar.mp4', )
        self.client = Client()

    def test_get_all_movie(self):
        response = self.client.get('/movies/')
        print(response.data)
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['title'], 'Test Movie')

    def test_search(self):
        response = self.client.get('/movies/?search=Test')

        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['title'], 'Test Movie')

    def test_order_by_imdb(self):
        response = self.client.get('/movies/?order=imdb')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['title'], 'Test Movie')
