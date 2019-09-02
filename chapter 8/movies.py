movies=[]
movie={}
movie['name']='Forbidden Planet'
movie['year']='1957'
movie['rating']='*****'
movies.append(movie)
movies2={'name': 'I was a Teenage Wolf', 'year': '1957', 'rating': '***'}
movies3={'name': 'viking women and the sea serpent', 'year': '1957', 'rating': '**'}
movies4={'name': 'vertigo', 'year': '1958', 'rating': '*****'}
movies.append(movies2)
movies.append(movies3)
movies.append(movies4)
print('Head first Movie recommendation')
print('-------------------------------')
for movie in movies:
	if len(movie['rating'])>=4:
		print(movie['name'],'('+movie['rating']+')', movie['year'])
		
