from django.db.models import Q
from .models import Room
from django.contrib.auth.decorators import login_required
from application.models import Account
import datetime
from pytz import timezone

tz = timezone("EST")


def getFormattedTime(timestamp):
    today = datetime.datetime.now(tz).date()
    yesterday = today - datetime.timedelta(days=1)
    if timestamp.date() == today:
        delta = datetime.datetime.now(tz) - timestamp
        hours_ago = int(delta.total_seconds()) // 3600
        if hours_ago == 1:
            return f"{hours_ago} hour ago"
        if hours_ago > 12:
            return "Today"
        if hours_ago > 1:
            return f"{hours_ago} hours ago"
        mins_ago = int(delta.total_seconds()) // 60
        if mins_ago == 0:
            return "Now"
        if mins_ago == 1:
            return f"{mins_ago} minute ago"
        return f"{mins_ago} minutes ago"
    elif timestamp.date() == yesterday:
        return "Yesterday"
    return timestamp.strftime("%m/%d")


@login_required
def chat_history(request, matched_pks):
    response = []
    rooms = Room.objects.filter(
        (Q(started_by=request.user) | Q(started_for=request.user))
    )
    for r in rooms:
        friend = r.started_by if r.started_by != request.user else r.started_for
        if friend.pk in matched_pks:
            friend_account = Account.objects.get(user=friend)
            latest_message = r.messages.last()
            latest_message_content = None
            time = None
            og_time = None
            if latest_message is not None:
                latest_message_content = latest_message.content
                time = getFormattedTime(latest_message.timestamp)
                if len(latest_message_content) > 25:
                    latest_message_content = f"{latest_message_content[:25]}..."
                og_time = latest_message.timestamp
                unread_messages = r.messages.filter(
                    Q(is_read=False) & Q(author=friend)
                ).count()
                response.append(
                    {
                        "friend_pk": friend.pk,
                        "latest_message": latest_message_content,
                        "friend_picture": friend_account.profile_picture.url,
                        "friend_name": f"{friend_account.first_name} {friend_account.last_name}",
                        "timestamp": time,
                        "unread_messages": unread_messages,
                        "original_time": og_time,
                    }
                )
    return sorted(response, key=lambda k: k["original_time"], reverse=True)
