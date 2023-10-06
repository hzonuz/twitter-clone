from django.db import models


# Create your models here.
class Tweet(models.Model):
    body = models.TextField()
    # media
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField("users.User", related_name="liked")
    bookmark = models.ManyToManyField("users.User", related_name="bookmarked")
    # retweet = models.ManyToManyField("users.User", related_name="retweeted")
    # quoted_tweet
    parent = models.ForeignKey("tweets.Tweet", related_name="comments",
                               on_delete=models.SET_NULL, null=True, blank=True)
    # mentioned_users = models.ManyToManyField("users.User")
