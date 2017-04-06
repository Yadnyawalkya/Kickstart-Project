from flask import Flask, redirect, url_for, request, render_template
import os
import crypt

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    fo = open("kickstart.cfg", "a+")
    if request.method == 'POST':
        if request.form['save'] == 'save':
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
            print(timezone)

            fo.write("\n# System timezone\ntimezone " + timezone + "")

            rootpass = request.form['pass']
            rerootpass = request.form['repass']
            check_en = request.form.to_dict('basic_encrypt')
            onoff_en = check_en['basic_encrypt']
            if onoff_en == 'check':
                if rootpass == rerootpass:
                    fo.write(
                        "\n# Root password\nrootpw --iscrypted " + crypt.crypt(rerootpass,
                                                                               crypt.mksalt(crypt.METHOD_MD5)))
            elif onoff_en == 'uncheck':
                fo.write("\n# Root password\nrootpw --plaintext " + rerootpass)

            ###Display Configuration
            fo.write("\n# Use graphical install\ngraphical")
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
                fo.write(
                    "\n# Run the Setup Agent on first boot\nfirstboot --reconfig\n# Do not configure the X Window System\nskipx")
            fo.close()
            return render_template('index.html')

        elif request.form['forthbutton'] == 'setup':
            print("setup madhye gelo")
            return render_template('setup.html')

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


