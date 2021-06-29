from typing import Dict
from flask import Flask
from flask import request
from flask import jsonify
import demo


_app = Flask(__name__)

_url = "/<path:service_type>"


@_app.route(_url, methods=["POST"])
def service(
        service_type: str,
) -> Dict[str, object]:

    json_dict = request.get_json()
    new_json_dict = demo.wrap(json_dict)
    return jsonify(new_json_dict)


if __name__ == "__main__":

    _app.run(debug=True)
