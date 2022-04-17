def navigation(request) -> dict:
    links = [{"title": "Из Москвы", "link": "/departure/msk/"}, {"title": "Из Петербурга", "link": "/departure/spb/"},
             {"title": "Из Новосибирска", "link": "/departure/nsk/"},
             {"title": "Из Екатеринбурга", "link": "/departure/ekb/"},
             {"title": "Из Казани", "link": "/departure/kazan/"}]
    return {"links": links}
