# from authentication.authentication import app

from client_image_processing.image_processing import app

from client_image_processing.add_purchases import app as app1


app.run(debug=True)
app1.run(debug=True)
