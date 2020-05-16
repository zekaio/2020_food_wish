# -*- coding: utf-8 -*-
from flask import session
from flask_restful import abort
import datetime
import models
from sqlalchemy.sql.expression import func
import typing
import random


# 获取user对象
def get_user(open_id: str) -> models.User:
    user: models.User = (
        models.User
            .query
            .filter_by(open_id=open_id)
            .first()
    )
    if not user:
        user: models.User = models.User(open_id=open_id)
        lott: models.Lottery = models.Lottery(open_id=open_id)
        models.db.session.add(lott)
        models.db.session.add(user)
        models.db.session.commit()
    elif user.update_day < datetime.date.today():
        user.update_day = datetime.date.today()
        user.help = 3
        user.wish = 3
        models.db.session.add(user)
        models.db.session.commit()
    return user


# 获取用户信息
def get_user_info(open_id: str) -> dict:
    user = get_user(open_id)
    return user.to_dict()


# 随机抽取愿望，默认三条
def get_random_wish(open_id: str, limit: int = 3) -> typing.List[dict]:
    wishes: typing.List[models.Wishes] = (
        models.Wishes
            .query
            .filter(models.Wishes.open_id != open_id, models.Wishes.status == 0)
            .order_by(func.rand())
            .limit(limit)
            .all()
    )
    ret: list = list()
    for wish in wishes:
        ret.append(wish.to_dict())
    return ret


# 许愿
def make_wish(data: dict) -> None:
    user = get_user(data['open_id'])
    if not user.wish:
        abort(406, message="今日许愿次数已用完")
        return
    wish: models.Wishes = models.Wishes(**data)
    user.wish = user.wish - 1
    user.lottery = user.lottery + 1
    models.db.session.add(wish)
    models.db.session.add(user)
    models.db.session.commit()
    return


# 获取具体愿望内容
def get_specific_wish(wish_id):
    wish: models.Wishes = (
        models.Wishes
            .query
            .filter(models.Wishes.id == wish_id)
            .first()
    )
    return wish.to_dict()


# 帮助TA
def help_wish(wish_id: int, open_id: str) -> None:
    user = get_user(open_id)
    if not user.help:
        abort(406, message="今日助愿次数已用完")
        return
    wish: models.Wishes = (
        models.Wishes
            .query
            .filter(models.Wishes.id == wish_id)
            .first()
    )
    if not wish:
        abort(404, message="愿望不存在")
        return
    if wish.status:
        abort(404, message="愿望已被其他人领取")
        return
    if wish.open_id == str(open_id):
        abort(412, message="无法帮助自己的愿望")
        return
    wish.helper_openid = open_id
    wish.status = 1
    user.help = user.help - 1
    models.db.session.add(wish)
    models.db.session.add(user)
    models.db.session.commit()
    return


# 收藏夹，获取我的愿望
def get_my_wishes(open_id: str) -> typing.List[dict]:
    wishes: typing.List[models.Wishes] = (
        models.Wishes
            .query
            .filter(models.Wishes.open_id == open_id)
            .all()
    )
    ret: list = list()
    for wish in wishes:
        ret.append(wish.to_dict())
    return ret


# 收藏夹，获取我的助愿
def get_my_help(open_id: str) -> typing.List[dict]:
    wishes: typing.List[models.Wishes] = (
        models.Wishes
            .query
            .filter(models.Wishes.helper_openid == open_id)
            .all()
    )
    ret: list = list()
    for wish in wishes:
        ret.append(wish.to_dict())
    return ret


# 助愿者确认已实现
def helper_confirm_complete(wish_id: int, open_id: str) -> None:
    wish: models.Wishes = (
        models.Wishes
            .query
            .filter(models.Wishes.id == wish_id)
            .first()
    )
    if not wish:
        abort(404, message="愿望不存在")
    if wish.helper_openid != str(open_id):
        abort(406, message="这个愿望不是你领取的")
    if wish.status != 1:
        abort(409, message="愿望未被领取或已确认实现")
    wish.status = 2
    models.db.session.add(wish)
    models.db.session.commit()
    return


# 许愿者确认已完成
def wisher_confirm_complete(wish_id: int, open_id: str) -> None:
    wish: models.Wishes = (
        models.Wishes
            .query
            .filter(models.Wishes.id == wish_id)
            .first()
    )
    if not wish:
        abort(404, message="愿望不存在")
    if wish.open_id != str(open_id):
        abort(406, message="这个愿望不是你许的")
    if wish.status != 2:
        abort(409, message="助愿者还未确认已实现")
    wish.status = 3
    wisher = get_user(wish.open_id)
    helper = get_user(wish.helper_openid)
    wisher.post = wisher.post + 1
    helper.lottery = helper.lottery + 1
    models.db.session.add(wisher)
    models.db.session.add(helper)
    models.db.session.add(wish)
    models.db.session.commit()
    return


# 放弃愿望
def giveup_wish(wish_id: int, open_id: str) -> None:
    user = get_user(open_id)
    wish: models.Wishes = (
        models.Wishes
            .query
            .filter(models.Wishes.id == wish_id)
            .first()
    )
    if not wish:
        abort(404, message="愿望不存在")
    if wish.helper_openid != str(open_id):
        abort(406, message="这个愿望不是你领取的")
    if wish.status != 1 and wish.status != 2:
        abort(409, message="愿望未被领取或已确认实现")
    wish.status = 0
    wish.helper_openid = None
    user.help = user.help + 1
    models.db.session.add(user)
    models.db.session.add(wish)
    models.db.session.commit()
    return


# 抽奖
def lottery(open_id: str):
    user = get_user(open_id)
    if not user.lottery:
        abort(406, message="抽奖次数已用完")
        return
    lott: models.Lottery = (
        models.Lottery
            .query
            .filter(models.Lottery.open_id == open_id)
            .first()
    )
    incomplete: dict = lott.get_incomplete()
    if len(incomplete) == 0:
        abort(409, message="图鉴已集齐")
    key = list(incomplete)[random.randint(0, len(incomplete) - 1)]
    setattr(lott, 'food' + str(int(key) + 1), int(getattr(lott, 'food' + str(int(key) + 1))) + 1)
    user.lottery = user.lottery - 1
    models.db.session.add(user)
    models.db.session.add(lott)
    models.db.session.commit()
    return key


# 获取抽奖进度
def get_lottery_process(open_id: str) -> list:
    lott: models.Lottery = (
        models.Lottery
            .query
            .filter(models.Lottery.open_id == open_id)
            .first()
    )
    if not lott:
        get_user(open_id)
        ret = [0 for _ in range(8)]
    else:
        ret = lott.to_list()
    return ret


# 设置昵称
def set_username(username: str, open_id: str) -> None:
    user = get_user(open_id)
    if user.username:
        abort(406, message="已设置过昵称")
        return
    user.username = username
    models.db.session.add(user)
    models.db.session.commit()
    return


# 获取帖子
def get_posts(last: int, limit: int) -> typing.List[dict]:
    if not last:
        posts: typing.List[models.Posts] = (
            models.Posts
                .query
                .order_by(models.Posts.id.desc())
                .limit(limit)
                .all()
        )
    else:
        posts: typing.List[models.Posts] = (
            models.Posts
                .query
                .filter(models.Posts.id < last)
                .order_by(models.Posts.id.desc())
                .limit(limit)
                .all()
        )
    ret: list = list()
    for post in posts:
        d: dict = post.to_dict()
        pics: typing.List[models.Pics] = post.pics
        if pics:
            pics_path: list = list()
            for pic in pics:
                pics_path.append(pic.path)
            d['pics'] = pics_path
        else:
            d['pics'] = []
        ret.append(d)
    return ret


# 发表帖子
def send_post(data: dict, pics: list) -> None:
    user = get_user(data['open_id'])
    if not user.post:
        abort(406, message="发帖次数已用完")
        return
    if not user.username:
        abort(404, message="请先填写昵称")
        return
    data['name'] = user.username
    post = models.Posts(**data)
    user.lottery = user.lottery + 1
    user.post = user.post - 1
    models.db.session.add(user)
    models.db.session.add(post)
    models.db.session.commit()
    if pics:
        for pic in pics:
            models.db.session.add(models.Pics(path=pic, post_id=post.id))
        models.db.session.commit()
    return
