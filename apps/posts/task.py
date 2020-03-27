from config.celery import app
from apps.users.usecases import SendEmail
from apps.posts.consts import EmailTextPosts


@app.task
def main_schedule_task_comments(comment, post, author_user_email):

    SendEmail.send(
        author_user_email,
        EmailTextPosts.title.value,
        EmailTextPosts.MessageNewComment.value.format(comment, post)
    )
