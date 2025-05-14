# -------------------------------------------------------------------------- #
# Copyright 2025-present, Federation Manager, by Software Networks, i2CAT    #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #

"""
Federation Manager application
"""
import connexion
from flask import render_template
import encoder
from flask_mongoengine import MongoEngine
from configparser import ConfigParser


CONFIG = ConfigParser()
CONFIG.read("conf/config.cfg")
HOST = CONFIG.get("server", "host")
PORT = int(CONFIG.get("server", "port"))
MONGO_HOST = CONFIG.get("mongodb", "host")
MONGO_PORT = CONFIG.get("mongodb", "port")


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://' + MONGO_HOST + ':' + MONGO_PORT + '/federation-manager'
}
DB = MongoEngine(app.app)
app.add_api('swagger.yaml', arguments={'title': 'Federation Management Service'}, pythonic_params=True)


@app.route("/", methods=["GET"])
def documentation():
    """Endpoint to retrieve documentation"""
    return render_template("swaggerui.html")


def main():
    app.run(host=HOST, port=PORT, threaded=True)


if __name__ == '__main__':
    main()
