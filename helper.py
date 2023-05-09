from flask import Blueprint, jsonify, abort, make_response,request


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        message = jsonify(f"{cls.__name__} {model_id} is invalid")
        abort(make_response(message, 400))

    model = cls.query.get(model_id)
    
    if not model:
        message = jsonify(f"{cls.__name__} {model_id} not found")
        abort(make_response(message, 404))
        
    return model 