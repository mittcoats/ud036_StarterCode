import fresh_tomatoes
import media

# Construct all the movies
gladiator						= media.Movie("Gladiator",
																	"A betrayed soldier avenges his family",
																	"http://orig12.deviantart.net/62a7/f/2013/076/4/8/gladiator___fanmade_poster_by_kc_eazyworld-d5ycg6p.jpg",
																	"https://www.youtube.com/watch?v=owK1qxDselE&t=15s",
																	"Universal",
																	"Russel Crowe",
																	)

wedding_crashers		= media.Movie("Wedding Crashers",
																	"Two friends enjoy crashing summer weddings",
																	"http://www.impawards.com/2005/posters/wedding_crashers_ver1.jpg",
																	"https://www.youtube.com/watch?v=ZeUSo8voIXM",
																	"New Line Cinema",
																	"Owen Wilson",
																	)

hidden_figures			= media.Movie("Hidden Figures",
																	"A group of black women overcome racism to help NASA lunar missions",
																	"http://www.impawards.com/2016/posters/hidden_figures.jpg",
																	"https://www.youtube.com/watch?v=RK8xHq6dfAo",
																	"20th Century Fox",
																	"Octavia Spencer",
																	)

lord_of_the_rings		= media.Movie("Lord of the Rings",
																	"A young hobit must travel to middle earth to destroy a powerful weapon",
																	"http://www.movieartarena.com/imgs/lotr1final.jpg",
																	"https://www.youtube.com/watch?v=V75dMMIW2B4",
																	"New Line Cinema",
																	"Elijah Wood",
																	)

imitation_game			= media.Movie("Imitation Game",
																	"A peculiar mathematician breaks the German Enigma in WWII, and invents first computer",
																	"http://www.impawards.com/2014/posters/imitation_game_ver6_xxlg.jpg",
																	"https://www.youtube.com/watch?v=S5CjKEFb-sM",
																	"The Weinstein Company",
																	"B Cumberbatch",
																	)

up									= media.Movie("Up",
																	"A young boy takes an old man on an adventure",
																	"https://vignette3.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",
																	"https://www.youtube.com/watch?v=pkqzFUhGPJg",
																	"Disney",
																	"Ed Asner",
																	)

iron_man						= media.Movie("Iron Man",
																	"Marvel Hero, Tony Stark, invents the iron man suit",
																	"http://cdn.collider.com/wp-content/uploads/2015/04/iron-man-1-poster.jpg",
																	"https://www.youtube.com/watch?v=8hYlB38asDY",
																	"Paramount",
																	"Robert Downey Jr.",
																	)

the_dark_night			= media.Movie("The Dark Night",
																	"A peculiar young mathematician breaks the German Enigma in WWII, and invents first computer",
																	"http://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg",
																	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
																	"Warner Bros.",
																	"Christian Bale",
																	)

harry_potter				= media.Movie("Harry Potter",
																	"A special boy is chosen to bring down the dark lord",
																	"http://harrypotterfanzone.com/wp-content/2015/07/chamber-of-secrets-theatrical-poster.jpg",
																	"https://www.youtube.com/watch?v=PbdM1db3JbY",
																	"Warner Bros.",
																	"Daniel Radcliff",
																	)

senna								= media.Movie("Senna",
																	"The story of legendary F1 driver, Ayrton Senna",
																	"https://www.popoptiq.com/wp-content/uploads/2011/08/Senna-Poster.jpg",
																	"https://www.youtube.com/watch?v=QOQLeqRcgKc&list=PLGtd4CYaO-wJ5tECYr6EyBAYrBe50r9Gb",
																	"Universal",
																	"Ayrton Senna",
																	)

caddy_shack					= media.Movie("Caddy Shack",
																	"A lazy greens keeper spoofs the country club lifestyle",
																	"https://images-na.ssl-images-amazon.com/images/I/51qVp-dXLgL.jpg",
																	"https://www.youtube.com/watch?v=x9Nl39uWEYk",
																	"Warner Bros.",
																	"Bill Murray",
																	)

constant_gardener		= media.Movie("The Constant Gardener",
																	"A man navigates violent crime rings in Kenya to pursue his love",
																	"http://www.impawards.com/2005/posters/constant_gardener.jpg",
																	"https://www.youtube.com/watch?v=1l1lzzfpWFU",
																	"Focus Features",
																	"Ralph Fiennes",
																	)

# make array of movies to display
movies = [
					gladiator,
					wedding_crashers,
					hidden_figures,
					lord_of_the_rings,
					imitation_game,
					up,
					iron_man,
					the_dark_night,
					harry_potter,
					senna,
					caddy_shack,
					constant_gardener
]

# call method to build and launch html page
fresh_tomatoes.open_movies_page(movies)

