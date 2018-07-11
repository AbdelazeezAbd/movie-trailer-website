#import media.py file to use movie class
import media
#import fresh_tomatoes.py to run the movies on the brwoser using an HTML page
import fresh_tomatoes
#store movies data like : movie title, movie storyline, poster image, youtube trailer URL . in the variables using movie class
moana = media.movie('Moana',
                    'The story of a girl saved the forest from loss',
                    'https://is4-ssl.mzstatic.com/image/thumb/Video122/v4/62/a6/fc/62a6fcc6-fbda-4bf4-f6b4-8d5047e0caa4/source/227x227bb.jpg',
                    'https://www.youtube.com/watch?v=LKFuXETZUsI')

stephen = media.movie('Stephen Hawking',
                      'The story of a disabled scientist',
                      'http://idora.milliyet.com.tr/YeniAnaResim/2018/03/15/stephen-hawking-kimdir-stephen-hawking-in-hastaligi--11016737.Jpeg',
                      'https://www.youtube.com/watch?v=LUayjO_KgsQ')

Harry = media.movie('Harry Potter',
                    'the story is about Science fiction',
                    'https://nerdist.com/wp-content/uploads/2017/09/harry-potter-promo-image.jpeg',
                    'https://www.youtube.com/watch?v=VyHV0BRtdxo')
jungle = media.movie('the Jungle Book',
                     'A story about a boy living in the jungle',
                     'https://static.arageek.com/wp-content/uploads/the-jungle-book.jpg',
                     'https://www.youtube.com/watch?v=T_EN03fJIyY')
trojan = media.movie('Trojan Horse',
                     'the story is about the best plan in the history',
                     'https://filmmusiccentral.files.wordpress.com/2016/01/trojan-horse-troy-the-movie.jpg',
                     'https://www.youtube.com/watch?v=Td1uPq9K--E')
beautifulmind = media.movie('A Beautiful Mind',
                            'the story is about a clever person',
                            'https://is5-ssl.mzstatic.com/image/thumb/Video/v4/53/0a/8d/530a8dea-5a13-8e51-ec65-04ed8a1b2d37/source/1200x630bb.jpg',
                            'https://www.youtube.com/watch?v=WFJgUm7iOKw')
#store all the variables above in a list is called movies
movies = [moana, stephen, Harry, jungle, trojan, beautifulmind]
#display the movies list using open_movies_page function in the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
