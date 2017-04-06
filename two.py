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
        utc_check = "false"
        if request.form.get('utc_check'):
            utc_check = "true"
        if utc_check == "false":
            fo.write("\n# System timezone\ntimezone " + timezone + "")
        elif utc_check == "true":
            fo.write("\n# System timezone\ntimezone " + timezone + " --isUtc")
        print(timezone)

        rootpass = request.form['pass']
        rerootpass = request.form['repass']
	if rootpass == rerootpass:
		if request.form.get('basic_encrypt'):
			print("basic encrypt **true**")
			fo.write("\n# Root password\nrootpw --iscrypted " + crypt.crypt(rerootpass, crypt.mksalt(crypt.METHOD_MD5)))
		else:
			print("basic encrypt **false**")
			fo.write("\n# Root password\nrootpw --plaintext " + rerootpass)

	if request.form.get("reboot"):
            fo.write("\n# Reboot after installation\nreboot")
	else:
            fo.write("\n# Halt after installation\nhalt")

	if request.form.get("textmode"):
		fo.write("\n# Use text mode install\ntext")
	else:
		fo.write("\n# Use graphical install\ngraphical")

        ###Display Configuration
        check_value = request.form.to_dict('display_checkbox')
	if request.form.get("display_checkbox"):
		print("checked")
		first_boot = check_value['first-boot']
		if first_boot == 'Enabled':
			print("enable")
			fo.write("\n# Run the Setup Agent on first boot\nfirstboot --enable")
		elif first_boot == 'Disabled':
			print("disable")
			fo.write("\n# Run the Setup Agent on first boot\nfirstboot --disable")
		elif first_boot == 'Reconfigure':
			print("reconfigure")
			fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig")
        else:
            print("uncheck")
            fo.write("\n# Run the Setup Agent on first boot\nfirstboot --reconfig\n# Do not configure the X Window System\nskipx")

    return render_template('index.html')
    fo.close()


if __name__ == '__main__':
    app.run(debug=True)

