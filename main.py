from flask import (Flask, render_template, request, redirect, jsonify, url_for,
                   flash)
from flask import session as login_session

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('front_page.html')


@app.route('/projects')
def projects():
	return render_template('projects.html')


#------neighborhood map code start

@app.route('/neighborhoodMap')
def neighborhoodMap():
    return render_template('neighborhood-map.html')

#------neighborhood map code end

#--- parallax
@app.route('/parallax')
def parallax():
    return render_template('parallax.html')




#--------------section for catalogApp

@app.route('/catalogApp')
def catalogApp():
    return 'catalog-app'

#----end of catalogApp code



@app.route('/reactPlayground')
def reactPlayground():
    return render_template('reactPlayground.html')

# -------python for the controller app

@app.route('/controller-app-example', methods=['GET', 'POST'])
@app.route('/controller-app-example/', methods=['GET', 'POST'])
@app.route('/controller-app-example/<string:button_set>/', methods=['GET', 'POST'])
@app.route('/controller/<string:button_set>/<string:quad>/', methods=['GET', 'POST'])
@app.route('/controller/<string:button_set>/<string:quad>/<int:rack_id>/', methods=['GET', 'POST'])
@app.route('/controller/<string:button_set>/<string:quad>/<int:rack_id>/<string:slot_id>/', methods=['GET', 'POST'])
@app.route('/controller/<string:button_set>/<string:quad>/<int:rack_id>/<string:slot_id>/', methods=['GET', 'POST'])
@app.route('/controller/<string:button_set>/<string:quad>/<int:rack_id>/<string:slot_id>/', methods=['GET', 'POST'])

def controller_app_example(button_set="main", rack_id="0", slot_id="0", quad='noQuad'):
    if request.method == 'POST':
        print 'post detected!!!!'
        return render_template('controller-app-example.html', rack_id=rack_id, slot_id=slot_id, button_set=button_set, quad=quad)

    # if not rack_id:
    #    return "rack_id was undefined"
    print "button_set:"
    print button_set
    print "quad:"
    print quad 
    rack_macs = {"0":"device1", "1":"device2", 
                 "2":"device3", "3":"device4", 
                 "4":"device5", "5":"device6", 
                 "6":"device7", "7":"device8", 
                 "8":"device9", "9":"device10",
                 "10":"device11", "11":"device12",
                 "12":"device13", "13":"device14",
                 "14":"device15", "15":"device16",
                 "16":"device17", "17":"device18",
                 "18":"device19", "19":"device20",
                 "20":"device21", "21":"device22",
                 "22":"device23", "23":"device24",
                 "24":"device25", "25":"device26",
                 "26":"device27"}

    t9_trans = {"a":"2", "b":"22", "c":"222", "d":"3", "e":"33",
                        "f":"333", "g":"4", "h":"44", "i":"444",
                        "j":"5", "k":"55", "l":"555", "m":"6", "n":"66",
                        "o":"666", "p":"7", "q":"77", "r":"777",
                        "s":"7777", "t":"8", "u":"88", "v":"888", 
                        "w":"9", "x":"99", "y":"999", "z":"9999"
                        }
    
    #if button_set == "letters":
    #    return render_template("controller-app-example_letters.html", button_set=button_set, quad=quad)
    #elif button_set == "numbers":
    #    return render_template('controller_numbers.html', button_set=button_set, quad=quad)
    #else:
    #    return render_template('controller-app-example.html', button_set=button_set, quad=quad)


    print rack_macs.get(str(rack_id))
    print "slot id:"+str(slot_id)
    selectedRack = rack_macs.get(str(rack_id))
    if not selectedRack:
        print "checking quad"
        if quad != "true":
            print "No valid Rack Selected"
            flash("Please select Rack" )
            return render_template('controller-app-example.html', button_set=button_set, quad=quad)
    else:
        return render_template('controller-app-example.html', button_set=button_set, rack_id=rack_id, slot_id=slot_id, quad=quad)

    

    


@app.route('/main_api')
def main_api(button_set=0, quad=0, rack_id=0):
	return "main_api executed"
# -----end of code for controller app

if __name__ == '__main__':
    app.secret_key = 'super_secret_key1'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
