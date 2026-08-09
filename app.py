from flask import *

app = Flask(__name__)

# ==================== SEO: ROBOTS & SITEMAP ====================
# NOTE: these must be served from the domain ROOT (not /static/) for
# search engines to find them. Previously there was no route for
# either file, so https://jecyaniproperties.com/robots.txt and
# /sitemap.xml both 404'd even though robots.txt referenced the sitemap.

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt', mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap_xml():
    return Response(render_template('sitemap.xml'), mimetype='application/xml')

# ==================== MAIN PAGES ====================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/properties')
def estate():
    return render_template('properties.html')

@app.route('/invest')
def investment():
    return render_template('investment.html')

@app.route('/about')
def about():
    return render_template('about.html')

# ==================== CITY LOCATION PAGES ====================

@app.route('/land-for-sale-in-abuja')
def land_abuja():
    return render_template('land-for-sale-in-abuja.html')

@app.route('/land-for-sale-in-lagos')
def land_lagos():
    return render_template('land-for-sale-in-lagos.html')

@app.route('/land-for-sale-in-aba')
def land_aba():
    return render_template('land-for-sale-in-aba.html')

@app.route('/land-for-sale-in-asaba')
def land_asaba():
    return render_template('land-for-sale-in-asaba.html')

@app.route('/land-for-sale-in-enugu')
def land_enugu():
    return render_template('land-for-sale-in-enugu.html')

@app.route('/land-for-sale-in-port-harcourt')
def land_ph():
    return render_template('land-for-sale-in-port-harcourt.html')

@app.route('/land-for-sale-in-umuahia')
def land_umuahia():
    return render_template('land-for-sale-in-umuahia.html')

# ==================== INDIVIDUAL ESTATE PAGES ====================

# Abuja Estates
@app.route('/estates/gold-town-abuja')
def estate_gold_town():
    return render_template('estate-gold-town-abuja.html')

@app.route('/estates/ivy-gold-extension-abuja')
def estate_ivy_gold():
    return render_template('estate-ivy-gold-extension-abuja.html')

@app.route('/estates/nando-city-of-hope-abuja')
def estate_nando_city():
    return render_template('estate-nando-city-of-hope-abuja.html')

# Aba Estates
@app.route('/estates/juniper-phase-2-aba')
def estate_juniper_phase2():
    return render_template('estate-juniper-phase-2-aba.html')

@app.route('/estates/ivy-supreme-aba')
def estate_ivy_supreme():
    return render_template('estate-ivy-supreme-aba.html')

# Asaba Estates
@app.route('/estates/newtown-ibusa-asaba')
def estate_newtown_ibusa():
    return render_template('estate-newtown-ibusa-asaba.html')

@app.route('/estates/crystal-city-asaba')
def estate_crystal_city():
    return render_template('estate-crystal-city-asaba.html')

# Enugu Estates
@app.route('/estates/cedar-city-enugu')
def estate_cedar_city():
    return render_template('estate-cedar-city-enugu.html')

# Umuahia Estates (Existing)
@app.route('/estates/oakwood-city-umuahia')
def estate_oakwood():
    return render_template('estate-oakwood-city-umuahia.html')

# ==================== NEW UMUAHIA ESTATES ====================

@app.route('/estates/billionaire-estate-umuahia')
def estate_billionaire():
    return render_template('estate-billionaire-umuahia.html')

@app.route('/estates/amakama-federal-umuahia')
def estate_amakama_federal():
    return render_template('estate-amakama-federal-umuahia.html')

@app.route('/estates/amakama-housing-umuahia')
def estate_amakama_housing():
    return render_template('estate-amakama-housing-umuahia.html')

@app.route('/estates/ibb-estate-cof-umuahia')
def estate_ibb_cof():
    return render_template('estate-ibb-cof-umuahia.html')

@app.route('/estates/ibb-estate-umuahia')
def estate_ibb():
    return render_template('estate-ibb-umuahia.html')


if __name__ == '__main__':
    app.run(debug=True)