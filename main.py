#***************************************************************************************************
#This webpage features four main HTML pages:
#1. Home: Provides an introduction and overview of recent projects, along with a timeline and
#         contact information.
#2. Portfolio: Showcases projects grouped into categories such as Data Analytics, Dashboards,
#         Web Development, Infographics, Statistical Analysis, SQL, and GIS. Each category
#         includes a brief description of the required skills, and clicking on an image reveals
#         complete project details.
#3. Resume: Offers comprehensive details of skills, education, experience, and more.
#4. Contact: Includes links to social media profiles, phone number, and email address.
#
#Each page includes a menu for easy navigation and a link at the top for smooth scrolling within
#the page.
#***************************************************************************************************

from flask import Flask, render_template

app = Flask('app')

#################### MAIN PAGES ####################


# Render Home
@app.route('/')
def home():
  return render_template('index.html')


# Render Portfolio
@app.route('/portfolio')
def portfolio():
  return render_template('portfolio.html')


# Render Resume
@app.route('/resume')
def resume():
  return render_template('resume.html')


# Render Contacts
@app.route('/contact')
def contact():
  return render_template('contact.html')


#################### PORTFOLIO ####################


##### Data Analytics Projects
# Render HEAD: Facility Maintenace
@app.route('/dataanalytics1')
def projectData1():
  return render_template('projectData1.html')


# Render Air Quality
@app.route('/dataanalytics2')
def projectData2():
  return render_template('projectData2.html')


# Render Crime Rate
@app.route('/dataanalytics3')
def projectData3():
  return render_template('projectData3.html')


# Render McDonald's Financial Statement
@app.route('/dataanalytics4')
def projectData4():
  return render_template('projectData4.html')


##### Dashboards
# Render AmazingMArt EU
@app.route('/dashboard1')
def dashboard1():
  return render_template('projectDash1.html')


# Render Oil Reserves
@app.route('/dashboard2')
def dashboard2():
  return render_template('projectDash2.html')


##### Web Development
# Render Send Message with Twilio
@app.route('/webdev1')
def webdev1():
  return render_template('projectWeb1.html')


# Render Currency Rates
@app.route('/webdev2')
def webdev2():
  return render_template('projectWeb2.html')


# Render Currency Rates
@app.route('/webdev3')
def webdev3():
  return render_template('projectWeb3.html')


##### Infographics
# Render Housing Crisis
@app.route('/infographic1')
def infographic1():
  return render_template('projectInfo1.html')


# Render Cigarette
@app.route('/infographic2')
def infographic2():
  return render_template('projectInfo2.html')


##### Statistical Analysis
# Render
@app.route('/stat1')
def stat1():
  return render_template('projectStat1.html')


##### SQL
# Render Pysical Data Model
@app.route('/sql1')
def sql1():
  return render_template('projectSQL1.html')


##### GIS
# Render Coniston Robbery Map
@app.route('/gis1')
def gis1():
  return render_template('projectGIS1.html')


app.run(host='0.0.0.0', port=8080)
