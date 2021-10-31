from recsys.models import UserProductView


class RecSysService(object):
    @staticmethod
    def increase_view_count(user_id, product_id):
        """
        Increase the view count of a product by 1.
        """
        try:
            productView = UserProductView.objects.get(user_id=user_id, product_id=product_id)
        except UserProductView.DoesNotExist:
            productView = UserProductView()
          
        productView.count += 1
        productView.save()

    @staticmethod
    def rating_product(self, rating):
        self.rating = rating
        self.save()
