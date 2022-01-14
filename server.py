import os
import requests
import utils
import time
import numpy as np
from flask import Flask, render_template, g, request

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
countries = utils._get_countries()
time.sleep(1)
confirmed, recovered, critical, deaths = utils._get_totals()
time.sleep(1)
news_list = utils._get_news()

@app.route('/')
def index():
    
    num_countries = len(countries)

    context = {"country_names":countries,
               "num_countries": num_countries,
               "confirmed": confirmed,
               "recovered": recovered,
               "critical": critical,
               "deaths": deaths,
               "news_lst": news_list}
    return render_template("index.html", **context)


@app.route('/country')
def country_stats():
    country = request.args.get("name")
    
    data = utils._get_country_stats(country)[0]
    
    _log = lambda num : 0 if num == 0 else np.log(num)
    context = {"country": country,
               "country_names": countries,
               "confirmed": confirmed,
               "recovered": recovered,
               "critical": critical,
               "deaths": deaths,
               "_recovered": data["recovered"],
               "_critical": data["critical"],
               "_deaths": data["deaths"],
               "_confirmed": data["confirmed"],
               "ln_recovered": _log(data["recovered"]),
               "ln_critical": _log(data["critical"]),
               "ln_deaths": _log(data["deaths"]),
               "ln_confirmed": _log(data["confirmed"]),
               "lnrecovered": _log(recovered),
               "lncritical": _log(critical),
               "lndeaths": _log(deaths),
               "lnconfirmed": _log(confirmed)}
    return render_template("country.html", **context)


if __name__ == "__main__":

    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=8111, threaded=True)


