from django.conf.urls.static import static
from recsys.models import ProductRating, UserProductView

import csv

class RecSysService(object):
    @staticmethod
    def increase_view_count(user, product):
        """
        Increase the view count of a product by 1.
        """
        try:
            productView = UserProductView.objects.get(user_id=user, product_id=product)
        except UserProductView.DoesNotExist:
            productView = UserProductView()
            productView.user_id = user
            productView.product_id = product
          
        productView.count += 1
        productView.save()

    @staticmethod
    def rating_product(self, rating):
        self.rating = rating
        self.save()


    @staticmethod
    def export_rating_to_csv():
        """
        Export the rating data to a csv file.
        """
        fields = ['user_id', 'product_id', 'rating']
        rows = []
        for rating in ProductRating.objects.all():
            rows.append([rating.user_id.id, rating.product_id.id, rating.rating])
        # write rows to csv file
        with open('ratings.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            writer.writerows(rows)
        
