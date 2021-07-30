from flask import Blueprint, jsonify, request
import stripe
import os

payments = Blueprint('payments', __name__)

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@payments.route('/pay', methods=['POST'])
def pay():
    """
    Receives payment amount from react app (client)
    creates paymentIntent with stripe
    returns the required paymentIntent and client secret
    """
    data = request.get_json()
    print(data)
    intent = stripe.PaymentIntent.create(amount=data['amnt'], currency='usd', metadata={'integration_check': 'accept_a_payment'})
    return jsonify(client_secret=intent.client_secret)