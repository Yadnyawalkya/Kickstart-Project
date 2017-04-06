from flask import Flask, redirect, url_for, request, render_template
import os
import crypt

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    fo = open("kickstart.cfg", "a+")
    if request.method == 'POST':

        ###Basic Configuration
        get_target = request.form.to_dict('target_architecture')
        target_architecture = get_target['target_architecture']
        print(target_architecture)
        fo.write("\n#platform=" + target_architecture + "")

        get_keyboard = request.form.to_dict('keyboard')
        keyboard = get_keyboard['keyboard']
        print(keyboard)
        fo.write("\n# Keyboard layouts\nkeyboard '" + keyboard + "'")

        get_language = request.form.to_dict('language')
        language = get_language['language']
        print(language)
        fo.write("\n# System language\n" + language + "")

        get_timezone = request.form.to_dict('timezone')
        timezone = get_timezone['timezone']
        check_utc = request.form.to_dict('utc_checkbox')
     	onoff_utc = check_utc['utc_checkbox']
        print(check_utc)
       	print(onoff_utc)
      	if onoff_utc == 'check':
            fo.write("\n# System timezone\ntimezone " + timezone + " --isUtc")
       	elif onoff_utc == 'uncheck':
            fo.write("\n# System timezone\ntimezone " + timezone + "")
        print(timezone)

       
        rootpass = request.form['pass']
        rerootpass = request.form['repass']
        check_en = request.form.to_dict('basic_encrypt')
        onoff_en = check_en['basic_encrypt']
        if onoff_en == 'check':
            if rootpass == rerootpass:
                fo.write("\n# Root password\nrootpw --iscrypted "+crypt.crypt(rerootpass,crypt.mksalt(crypt.METHOD_MD5)))
        elif onoff_en == 'uncheck':
            fo.write("\n# Root password\nrootpw --plaintext "+rerootpass)


        check_reboot = request.form.to_dict('reboot')
     	onoff_reboot = check_utc['reboot']
      	if onoff_reboot == 'check':
            fo.write("\n# Reboot after installation\nreboot")
       	elif onoff_reboot == 'uncheck':
            fo.write("\n# Halt after installation\nhalt")


        check_textmode = request.form.to_dict('textmode')
     	onoff_textmode = check_utc['textmode']
      	if onoff_textmode == 'check':
            fo.write("\n# Use text mode install\ntext")
       	elif onoff_textmode == 'uncheck':
            fo.write("\n# Use graphical install\ngraphical")

        
	###Display Configuration
        check_value = request.form.to_dict('display-checkbox')
        check_or_uncheck = check_value['display-checkbox']
        if check_or_uncheck == 'check':
            print("check")
            first_boot = check_value['first-boot']
            if first_boot == 'Enabled':
                print("enable")
                fo.write("\n# Run the Setup Agent on first boot\nfirstboot --enable")
            elif first_boot == 'Disabled':
                print("disable")
                fo.write("\nfirstboot --disable")
            elif first_boot == 'Reconfigure':
                print("reconfigure")
                fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig")
        elif check_or_uncheck == 'uncheck':
            print("uncheck")
            fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig\n# Do not configure the X Window System\nskipx")

    return render_template('index.html')
    fo.close()


if __name__ == '__main__':
    app.run(debug=True)

