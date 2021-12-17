import csv
from collections import defaultdict

import surprise
from django.conf.urls.static import static
from surprise import Dataset, KNNBasic, Reader

from recsys.models import ProductRating, UserProductView


class RecSysService(object):
    @staticmethod
    def increase_view_count(user, product):
        """
        Increase the view count of a product by 1.
        """
        try:
            productView = UserProductView.objects.get(
                user_id=user, product_id=product)
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
            rows.append(
                [rating.user_id.id, rating.product_id.id, rating.rating])
        # write rows to csv file
        with open('ratings.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            writer.writerows(rows)

    @staticmethod
    def export_view_to_csv():
        """
        Export the view data to a csv file.
        """
        fields = ['user_id', 'product_id', 'count']
        rows = []
        for view in UserProductView.objects.all():
            rows.append([view.user_id.id, view.product_id.id, view.count])
        # write rows to csv file
        with open('views.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fields)
            writer.writerows(rows)


def get_top_n(predictions, n=10):
    """Return the top-N recommendation for each user from a set of predictions.

    Args:
        predictions(list of Prediction objects): The list of predictions, as
            returned by the test method of an algorithm.
        n(int): The number of recommendation to output for each user. Default
            is 10.

    Returns:
    A dict where keys are user (raw) ids and values are lists of tuples:
        [(raw item id, rating estimation), ...] of size n.
    """

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


class RecSysModel:
    def __init__(self):
        if RecSysModel.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.rating_model = None
            RecSysModel.__instance = self
    __instance = None

    @staticmethod
    def instance():
        if RecSysModel.__instance is None:
            RecSysModel()
        return RecSysModel.__instance

    # train by rating
    def train(self):
        rating_file = "views.csv"
        rating_reader = Reader(
            line_format="user item rating", sep=',', skip_lines=1)
        data = Dataset.load_from_file(rating_file, rating_reader)
        rating_training_set = data.build_full_trainset()
        sim_options = {'name': 'pearson_baseline', 'user_based': False}
        self.rating_algo = KNNBasic(sim_options=sim_options)
        self.rating_algo.fit(rating_training_set)

        # predict rating for all pairs (u, i) that are NOT in the training set
        rating_test_set = rating_training_set.build_anti_testset()
        print(rating_training_set.all_users())
        self.predictions = self.rating_algo.test(rating_test_set)
        # top 10 item
        self.top_n = get_top_n(self.predictions, 10)
        print(self.top_n)

    # train by viewing
    def train_by_view(self):
        pass

    def get_most_similar_item(self, item_id):
        pass

    def top_item_by_rating(self, user_id):
        """
        return top-10 recommendations for user `user_id`
        """
        try:
            if not self.top_n and not self.top_n.get(str(user_id)):
                return []
            return list(map(lambda x: int(x[0]), self.top_n[str(user_id)]))
        except Exception as e:
            return []

    def related_items(self, item_id):
        """
        return related items for item `item_id`
        """
        try:
            item_id = self.rating_algo.trainset.to_inner_iid(str(item_id))
            inner_ids = self.rating_algo.get_neighbors(item_id, k=5)
            return list(map(lambda x: self.rating_algo.trainset.to_raw_iid(x), inner_ids))
        except Exception as e:
            return []
