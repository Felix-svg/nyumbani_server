from config import app, api
from models.contact_information import ContactInformation
from routes.home import Home
from routes.reviews import Reviews
from routes.listings import ListingByID, Listings

# Routes
api.add_resource(Home, "/")
api.add_resource(Reviews, "/reviews")
api.add_resource(Listings, "/listings")
api.add_resource(ListingByID, "/listings/<int:id>")


if __name__ == "__main__":
    app.run()
