from flask import (Flask, render_template, request, redirect, jsonify, url_for,
                   flash)
from flask import session as login_session

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('front_page.html')

@app.route('/catalogApp')
def catalogApp():
	return "PlaceHolder for Catalog App"

@app.route('/projects')
def projects():
	return render_template('projects.html')

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
def controller_app_example(button_set="main", rack_id="0", slot_id="0", quad='noQuad'):
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


    

    if request.method == 'POST':
        if not selectedRack:
            if quad != "true":
                print "No valid Rack Selected"
                flash("Please select Rack")
                return render_template('controller-app-example.html', button=button_set, quad=quad)  

        test=request.form.to_dict()
        print "POST Data:"+str(test)
        
        # function for implementing sending to two racks at once
        #ke
        #ksTest = request.form.get('keySendTest')
        #print ksTest
        #if ksTest == "qwerty":
        #    testList = {
        #                "rack":"rack1",
        ##                "command":"menu",
        #                "slot":"1"
        #                }
                        
        #    keySendv3(testList)
        #    return "kstest executed"



        # Validation for slot id
        if slot_id != "0":
            print "slot id detected"
            slotVar = str(slot_id)
            print "slotVar:"+str(slotVar)
        else:
            print "no slot id detected, sending command to all stbs in rack"
            slotVar = "1-16"
        var1 = test.get('name', '')
        print "var1:"
        print var1
        alphaVar = test.get('name2', '')
        
        keyword = test.get('keyword', '')
        print keyword
        #------
        print "quad mode:" + str(quad)
      
        # check for keyword flag
        if keyword:
            print keyword
            check=""
            for letter in keyword:
                    print "letter:"+letter
                    digitVer = t9_trans.get(letter)
                    print "digitVer:"+digitVer
                    testArray = []
                    for char in digitVer:
                        print "Char:" + char
                        testArray.append(char)
                        #keySendv2(selectedRack, k, slotVar)
                    print testArray
                    print "char after loop:" +char
                    if check == char:
                        print "comparision passed!"
                        #time.sleep(5)
                        keySendv2(selectedRack, "rightArrow", slotVar)
                    # sENd ir command
                    for testArrayItem in testArray:
                        print "testArrayItem:"+testArrayItem
                        keySendv2(selectedRack, testArrayItem, slotVar)
                    print "last number command sent:"+testArrayItem
                    check = testArrayItem
            pass
        

        if var1:
            print 'detected value in var1'
            if var1.isnumeric():
                print "numeric command detected, iterating through numbers before sending commands"
                print "quad mode:" + str(quad)
                if quad == 'true':
                    print rack_macs["3"]
                    for c in var1:
                        keySendv2(rack_macs["3"], c, '1,2,9,8')
                        keySendv2(rack_macs["2"], c, '1,2,3,4,5,6,9,10,11,14,15,16')
                    return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id)
                else:
                    for c in var1:
                        keySendv2(selectedRack, c, slotVar)
                    return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id)
            else:
                print "command string detected, sending command directly"
                if quad == 'true':
                    keySendv2(rack_macs["3"], var1, '1,2,9,8')
                    keySendv2(rack_macs["2"], var1, '1,2,3,4,5,6,9,10,11,14,15,16')
                    #return render_template('controller-app-example.html')
                else:
                    print "slot var:"
                    print slotVar
                    keySendv2(selectedRack, var1, slotVar)
        elif alphaVar:
            print 'name2 contents: '+ alphaVar
          
            if alphaVar in t9_trans:
                print 'valid letter input found, translating to t9'
                for i in t9_trans.get(alphaVar):
                    keySendv2(selectedRack, i, slotVar)
                return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id) 
            else:
                message = 'invalid input detected, command was not sent'
                print message
                return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id, error=message)    
        else:
            message = 'Error with Post Data Input'
            print 'Error with Post Data Input'
            return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id, error=message)
        return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id)
    else:
        print "request was not POST"
        return render_template('controller-app-example.html', button_set=button_set, quad=quad, rack_id=rack_id, slot_id=slot_id)
@app.route('/main_api')
def main_api(button_set=0, quad=0, rack_id=0):
	return "main_api executed"
# -----end of code for controller app

if __name__ == '__main__':
    app.secret_key = 'super_secret_key1'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
